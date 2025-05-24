# Building AI Video Agents with LiveKit: From Zero to Production

## Video Title
"Building AI Video Agents in 15 Minutes: The Complete LiveKit Guide"

## Hook
"Want to build an AI assistant that can actually see and troubleshoot problems? In this video, I'll show you how to create a full-featured video AI agent using LiveKit in just 15 minutes. You'll learn how to give your AI real eyes and ears with surprisingly little code. I'll demonstrate two real scenarios where the agent visually identifies problems on screen and guides users through step-by-step solutions - just like having a technical support expert who can see exactly what you're seeing."

## Introduction (1-2 minutes)
- Welcome viewers and introduce yourself
- Explain what LiveKit is: "LiveKit is an open-source platform that makes building real-time applications with video, audio, and data capabilities incredibly easy."
- Set expectations: "By the end of this video, you'll have a fully functional AI video agent that can see and hear you, plus understand how to customize it for your own needs."
- Show a quick demo of the final product

## Section 1: Understanding the Architecture (2-3 minutes)
- Explain the components:
  - LiveKit server: Handles all the video/audio streaming
  - Python agent backend: Controls the AI's behavior
  - React frontend: What users interact with
- Walk through the architecture diagram (optional)
- Explain how the components work together
- Key point: "This modular approach means you can easily swap pieces as needed"

## Section 2: Setting Up the Backend (4-5 minutes)

### **FastAPI Token Server (1-2 minutes)**
- Show the `api.py` file - this is production-ready room management
- Key features:
  - **Automatic room creation** with unique UUIDs for each session
  - **JWT token generation** with proper video grants (publish, subscribe, join)
  - **Environment-based configuration** - securely loads LiveKit credentials
  - **CORS setup** for cross-origin requests from your frontend
- Highlight: "This isn't just demo code - this is exactly how you'd handle authentication in production"

### **Video Agent Core (2-3 minutes)**
- Walk through the `video_agent.py` file 
- Explain key components:
  - Agent class and AI model configuration
  - Speech-to-Text (Deepgram), Text-to-Speech (Cartesia), LLM (GPT-4)
  - Knowledge base integration for domain expertise
- **Intelligent Frame Processing**:
  - Only captures frames when user is speaking (1fps sampling rate)
  - Strategic frame selection: most recent + first + middle for longer conversations
  - Automatic memory management (clears frames when user starts new speech)
  - Sends multiple frames to GPT-4 for better visual context
- **LiveKit Workers Architecture**:
  - Show the `cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))` line
  - Explain: "You can run multiple instances of this worker across different servers"
  - LiveKit automatically distributes incoming sessions across available workers
  - Perfect for scaling: "Need to handle more users? Just spin up more workers"
  - No load balancer needed - LiveKit handles all the orchestration
- **Full Control vs. Real-time APIs**:
  - Show the `llm_node` method where we modify the chat context
  - Explain: "Unlike OpenAI's real-time API or ElevenLabs conversational agents, you have complete control"
  - You decide exactly what goes to the LLM and when - context, images, conversation history
  - Can add custom logic, filtering, or pre-processing before LLM calls
  - Trade-off: More control means more complexity and potential latency
  - "This flexibility is crucial for specialized use cases like visual troubleshooting"
- Emphasize: "LiveKit gives you the building blocks - you control the intelligence"

## Section 3: Building the Frontend (3-4 minutes)
- Show how to use LiveKit Components to build a video interface
- Walk through the React components
- Demonstrate the simplicity of the `<LiveKitRoom>` and `<VideoConference>` components
- Show how to handle room connections and tokens

## Section 4: Plugin System and Customization (3-4 minutes)
- Explain LiveKit's plugin architecture:
  - "One of the most powerful features of LiveKit is its plugin system that lets you easily swap different AI components"
  - Show the imports in our code and explain each component:
    - **Speech-to-Text (STT)**: We're using Deepgram, but LiveKit supports many options:
      - Amazon Transcribe, AssemblyAI, Azure AI Speech, Clova, Deepgram, fal, Gladia, Google Cloud, Groq, OpenAI, Speechmatics
      - "You can choose based on accuracy, latency, language support, or cost"
    - **Large Language Models (LLM)**: We're using OpenAI, but you can use:
      - Amazon Bedrock, Anthropic (Claude), Google Gemini, Groq, Azure OpenAI, Cerebras, DeepSeek, Fireworks, Ollama, Perplexity, Together AI, xAI (Grok)
      - "Pick the model that best fits your specific needs and budget"
    - **Text-to-Speech (TTS)**: We're using Cartesia, but other options include:
      - Amazon Polly, Azure AI Speech, Deepgram, ElevenLabs, Google Cloud, Groq, Neuphonic, OpenAI, PlayHT, Resemble AI, Rime, Speechify
      - "Choose based on voice quality, emotion control, or multilingual support"
    - **Voice Activity Detection (VAD)**: We're using Silero, which runs locally for privacy and low latency
  - Emphasize how easy it is to swap components: "Just change a couple lines of code"
- **Creating Custom Plugins**:
  - "What if you need a provider that's not built-in? You can create your own plugins"
  - Show the plugin interface pattern - inherit from base classes like `STT`, `LLM`, or `TTS`
  - Example: "Want to use a proprietary speech model? Create a custom STT plugin"
  - "Need to integrate with your company's LLM? Build a custom LLM plugin"
  - Plugin system ensures your custom solutions work seamlessly with LiveKit's infrastructure
  - "This means you're never locked into specific providers - total flexibility"

## Section 5: Advanced Features (3-4 minutes)
- **Knowledge Base System**:
  - Show the markdown files (dashboard.md, export.md, permissions.md) 
  - Explain how the KnowledgeManager loads and formats content
  - Demonstrate how knowledge gets injected into agent instructions
  - Show specific troubleshooting steps that match our demo scenarios
- **Visual Frame Processing**:
  - Explain how agent captures frames when user speaks
  - Show the frame selection logic (most recent, first, middle)
  - Highlight how images are sent to GPT-4 with high detail
- **Langfuse Observability**:
  - Walk through the Langfuse dashboard showing actual traces
  - Show STT, LLM, and TTS spans with timing and costs
  - Explain how this helps optimize performance in production
- Emphasize how these features make the agent truly production-ready

## Section 6: Demo - Technical Support Agent (4-5 minutes)
- Showcase the complete application with two real demo scenarios
- **Demo Setup**: 
  - Open CloudDash (our demo analytics platform)
  - Start LiveKit session and enable screen sharing
  - Show the agent is ready to help

### **Scenario 1: Widget Configuration Issue (2 minutes)**
- **Show the problem**: Point to the broken "Performance Metrics" widget with red "ERROR: NO DATA"
- **Ask for help**: "Can you help me fix this widget that's not working?"
- **Agent response**: Watch agent identify the error, read the current refresh rate (1 hour), and diagnose the issue
- **Follow guidance**: Agent guides you to click the gear icon and change refresh rate to 5 minutes
- **Success**: Widget displays data and shows confirmation message

### **Scenario 2: Export Size Exceeded Error (2 minutes)**
- **Navigate to Data Export**: Show the export form with default settings
- **Trigger the error**: Click "Generate Export" to show the size exceeded error
- **Ask for help**: "I'm getting an export error, can you help?"
- **Agent response**: Watch agent read the error details (25,000 rows, CSV 10,000 limit) and provide solution
- **Follow guidance**: Agent guides you to select XLSX format instead of CSV
- **Success**: Export succeeds with success message

### **Key Demo Points**:
- **Visual Problem Solving**: Agent sees and describes specific UI elements and errors
- **Knowledge Integration**: Agent uses built-in troubleshooting guides to provide accurate solutions
- **Step-by-step guidance**: Agent breaks down fixes into clear, actionable steps
- **Natural interaction**: Feels like talking to a real technical support specialist

## Conclusion (1-2 minutes)
- Recap what we've built
- Highlight key advantages of using LiveKit:
  - Fast development
  - Production-ready
  - Easily customizable with the plugin system
  - Open source
- Emphasize API requirements:
  - "You'll need to sign up for the services we've used: LiveKit, OpenAI, Deepgram, Cartesia, and Langfuse"
  - "All of these offer free tiers to get started"
  - "For observability, we're using Langfuse which gives you great insights into your agent's performance"
  - "Remember, you can swap any component with a different provider using LiveKit's plugin system"
- Discuss business applications:
  - Technical support and troubleshooting (as we demonstrated)
  - Customer onboarding for complex products
  - Remote equipment installation guidance
  - Professional services consulting
  - Software training and education
- Highlight ROI potential:
  - Reduced support costs through automation
  - Improved first-contact resolution rates
  - Faster time-to-resolution for technical issues
  - Scalable expertise without proportional staffing
- Call to action:
  - Like and subscribe
  - Check out LiveKit's documentation
  - Contact me for consulting on implementing AI solutions for your business challenges

## Additional Production Notes
- **B-roll**: Include clips of the agent interacting with different scenarios
- **Graphics**: Include architecture diagram and key concept visualizations
- **Text overlays**: Highlight key code snippets and configuration parameters
- **Timestamps**: Add chapter markers for easy navigation
- **Resource links**: Include links to LiveKit documentation, GitHub repo, and other resources

## Key Talking Points to Emphasize
1. LiveKit makes video/audio AI accessible to any developer
2. The modular architecture makes it easy to customize
3. From prototype to production with minimal code
4. The importance of observability for AI systems
5. Contextual knowledge integration enhances the agent's capabilities
6. Visual technical support provides tremendous business value
7. AI agents can reduce operational costs while improving customer experience