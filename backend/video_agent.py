import asyncio
import logging
import time
import io
from datetime import UTC, datetime
from typing import Union, AsyncIterable, Optional, List
from uuid import uuid4

from dotenv import load_dotenv
from langfuse import Langfuse
from langfuse.client import StatefulClient

from livekit import rtc
from livekit.agents import (
    Agent,
    AgentSession,
    ChatContext,
    ChatMessage,
    JobContext,
    FunctionTool,
    ModelSettings,
    RoomInputOptions,
    RoomOutputOptions,
    WorkerOptions,
    UserStateChangedEvent,
    cli,
    stt,
    llm,
)
from livekit.agents.llm import ImageContent, AudioContent
from livekit.plugins import cartesia, deepgram, openai, silero
from livekit.plugins.turn_detector.english import EnglishModel
from knowledge_manager import KnowledgeManager

logger = logging.getLogger("openai-video-agent")
logger.setLevel(logging.INFO)

load_dotenv()

_langfuse = Langfuse()

# Initialize knowledge manager
knowledge_manager = KnowledgeManager()

INSTRUCTIONS = f"""
You are a technical support AI specialist who can see the user's screen through video. 
Your role is to provide real-time visual assistance for software troubleshooting.

Key responsibilities:
- Identify what's on the user's screen (UI elements, error messages, settings)
- Guide users through navigation with clear, step-by-step instructions
- Reference relevant documentation when needed
- Provide precise guidance based on what you can see
- Maintain a friendly, patient, and supportive tone

When you see a user's screen:
1. First acknowledge what you can see ("I can see you're in the Settings menu")
2. Identify any visible issues or areas for improvement
3. Provide clear instructions on what to do next

For our demo, assume the user is working with "CloudDash" - a fictional SaaS analytics platform.
Common issues include incorrect export settings, permission issues, dashboard configuration problems,
and navigation confusion. Adapt to whatever the user is showing you.

{knowledge_manager.format_knowledge()}
"""

class VideoAgent(Agent):
    def __init__(self, instructions: str, room: rtc.Room) -> None:
        super().__init__(
            instructions=instructions,
            llm=openai.LLM(model="gpt-4.1"),
            stt=deepgram.STT(),
            tts=cartesia.TTS(
                model="sonic-2",
                speed="fast",
                voice="bf0a246a-8642-498a-9950-80c35e9276b5",
            ),
            vad=silero.VAD.load(),
            turn_detection=EnglishModel(),
        )
        self.room = room
        self.session_id = str(uuid4())
        self.current_trace = None

        self.frames: List[rtc.VideoFrame] = []
        self.last_frame_time: float = 0
        self.video_stream: Optional[rtc.VideoStream] = None

    async def close(self) -> None:
        if self.video_stream:
            await self.video_stream.aclose()
            self.video_stream = None
        if self.current_trace:
            self.current_trace = None
        _langfuse.flush()

    async def on_enter(self) -> None:
        # Just generate a basic intro without video reference
        self.session.generate_reply(
            instructions="introduce yourself very briefly"
        )
        self.session.on("user_state_changed", self.on_user_state_change)
        self.room.on("track_subscribed", self.on_track_subscribed)

    async def on_exit(self) -> None:
        await self.session.generate_reply(
            instructions="tell the user a friendly goodbye before you exit",
        )
        await self.close()

    def get_current_trace(self) -> StatefulClient:
        if self.current_trace:
            return self.current_trace
        self.current_trace = _langfuse.trace(name="video_agent", session_id=self.session_id)
        return self.current_trace

    # Monitor state changes for the user
    def on_user_state_change(self, event: UserStateChangedEvent) -> None:
        old_state = event.old_state
        new_state = event.new_state
        print(f"USER STATE CHANGED: {old_state} -> {new_state}")

        # When user starts speaking, clear old frames
        if new_state == "speaking" and old_state != "speaking":
            self.frames = []
            print("User started speaking - cleared previous frames")
        
    async def on_user_turn_completed(
        self, turn_ctx: ChatContext, new_message: ChatMessage,
    ) -> None:
        # Reset the span when a new user turn is completed
        if self.current_trace:
            self.current_trace = None
        self.current_trace = _langfuse.trace(name="video_agent", session_id=self.session_id)
        logger.info(f"User turn completed {self.get_current_trace().trace_id}")

    async def stt_node(
        self, audio: AsyncIterable[rtc.AudioFrame], model_settings: ModelSettings
    ) -> Optional[AsyncIterable[stt.SpeechEvent]]:
        logger.info(f"STT node called {self.get_current_trace().trace_id}")
        span = self.get_current_trace().span(name="stt_node", metadata={"model": "deepgram"})
        try:
            async for event in Agent.default.stt_node(self, audio, model_settings):
                logger.info(f"STT event: {event.type} {event.request_id}")
                yield event
        except Exception as e:
            span.update(level="ERROR")
            logger.error(f"STT error: {e}")
            raise
        finally:
            span.end()

    async def llm_node(
        self,
        chat_ctx: llm.ChatContext,
        tools: List[FunctionTool],
        model_settings: ModelSettings
    ) -> AsyncIterable[llm.ChatChunk]:
        logger.info(f"LLM node called {self.get_current_trace().trace_id}")

        copied_ctx = chat_ctx.copy()
        frames_to_use = self.current_frames()

        for position, frame in frames_to_use:
            # Use the original frame for LLM context
            image_content = ImageContent(
                image=frame,
                inference_detail="high"
            )
            copied_ctx.add_message(
                role="user",
                content=[f"{position.title()} view of user during speech:", image_content]
            )
            print(f"ADDED {position.upper()} FRAME TO CHAT CONTEXT")
        else:
            print("WARNING: No captured frames available for this conversation")

        messages = openai.utils.to_chat_ctx(copied_ctx, cache_key=self.llm)
        
        generation = self.get_current_trace().generation(
            name="llm_generation",
            model="gpt-4.1",
            input=messages,
        )
        output = ""
        set_completion_start_time = False
        try:
            async for chunk in Agent.default.llm_node(self, copied_ctx, tools, model_settings):
                if not set_completion_start_time:
                    generation.update(
                        completion_start_time=datetime.now(UTC),
                    )
                    set_completion_start_time = True
                if chunk.delta and chunk.delta.content:
                    output += chunk.delta.content
                yield chunk
        except Exception as e:
            generation.update(level="ERROR")
            logger.error(f"LLM error: {e}")
            raise
        finally:
            generation.end(output=output)

    async def tts_node(
        self, text: AsyncIterable[str], model_settings: ModelSettings
    ) -> AsyncIterable[rtc.AudioFrame]:
        logger.info(f"TTS node called {self.get_current_trace().trace_id}")
        span = self.get_current_trace().span(name="tts_node", metadata={"model": "cartesia"})
        try:
            async for event in Agent.default.tts_node(self, text, model_settings):
                yield event
        except Exception as e:
            span.update(level="ERROR")
            logger.error(f"TTS error: {e}")
            raise
        finally:
            span.end()

    def on_track_subscribed(
        self,
        track: rtc.RemoteTrack,
        publication: rtc.RemoteTrackPublication,
        participant: rtc.RemoteParticipant,
    ) -> None:
        if publication.source != rtc.TrackSource.SOURCE_SCREENSHARE:
            return
        print("TRACK SUBSCRIBED")

        # start the new stream
        asyncio.create_task(self.read_video_stream(rtc.VideoStream(track)))

    async def read_video_stream(self, video_stream: rtc.VideoStream) -> None:
        # close open streams
        await self.close()
        self.video_stream = video_stream

        print("STARTING VIDEO FRAME SAMPLER")
        frame_count = 0
        async for event in video_stream:
            # Only capture frames when the user is speaking
            if self.session.user_state == "speaking":
                # Capture frames at 1 per second
                current_time = time.time()
                if current_time - self.last_frame_time >= 1.0:
                    # Store the frame and update time
                    frame = event.frame
                    self.frames.append(frame)
                    self.last_frame_time = current_time

                    frame_count += 1
                    print(f"CAPTURED FRAME #{frame_count}: {frame.width}x{frame.height}, type={rtc.VideoBufferType.Name(frame.type)}")
                    print(f"Total frames stored: {len(self.frames)}")
        print(f"VIDEO INPUT MONITOR ENDED after {frame_count} frames")

    def current_frames(self) -> List[rtc.VideoFrame]:
        # Add strategic frames from the conversation to provide better context
        # We'll use the first and last frames if available, plus a middle frame for longer sequences
        current_frames = []
        if len(self.frames) > 0:
            # Always use the most recent frame
            current_frames.append(("most recent", self.frames[-1]))

            # For sequences with multiple frames, also include the first frame
            if len(self.frames) >= 3:
                current_frames.append(("first", self.frames[0]))

                # For longer sequences (5+ frames), also include a middle frame
                if len(self.frames) >= 5:
                    mid_idx = len(self.frames) // 2
                    current_frames.append(("middle", self.frames[mid_idx]))
        print(f"ADDING {len(current_frames)} FRAMES TO CONVERSATION (from {len(self.frames)} available frames)")
        # return frames in reverse order so earliest frames appear first in context
        return list(reversed(current_frames))


async def entrypoint(ctx: JobContext) -> None:
    # Connect to the room
    await ctx.connect()

    print(f"CONNECTED TO ROOM: {ctx.room.name}")
    print(f"LOCAL PARTICIPANT: {ctx.room.local_participant.identity}")

    if len(ctx.room.remote_participants) == 0:
        print("EXITING: No remote participants in the room")
        return

    print(f"REMOTE PARTICIPANTS: {len(ctx.room.remote_participants)}")
    # Create a simple agent session without custom frame rate
    # Just use the default settings which should work fine
    session = AgentSession()

    # Configure agent
    agent = VideoAgent(instructions=INSTRUCTIONS, room=ctx.room)
    
    # Set up room input/output - explicitly enable all modes
    room_input = RoomInputOptions(
        video_enabled=True,
        audio_enabled=True
    )
    
    room_output = RoomOutputOptions(
        audio_enabled=True,
        transcription_enabled=True
    )

    # Start the agent with all capabilities
    await session.start(
        agent=agent,
        room=ctx.room,
        room_input_options=room_input,
        room_output_options=room_output,
    )


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
