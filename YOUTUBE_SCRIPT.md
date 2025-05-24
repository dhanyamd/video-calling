# Building AI Video Agents with LiveKit: From Zero to Production

## Video Title
"Building AI Video Agents in 15 Minutes: The Complete LiveKit Guide"

## Hook
"Want to build an AI assistant that can actually see? In this video, I'll show you how to create a full-featured video AI agent using LiveKit in just 15 minutes. You'll learn how to give your AI real eyes and ears with surprisingly little code. As a bonus, I'll demonstrate how this technology can transform technical support by creating an agent that can see and respond to what's happening on a user's screen, cutting support costs while improving the customer experience."

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

## Section 2: Setting Up the Backend (3-4 minutes)
- Walk through the Python code for the video agent
- Explain key components:
  - Agent class and settings
  - Speech-to-Text (Deepgram)
  - Text-to-Speech (Cartesia)
  - LLM (GPT-4o)
  - Room configuration
- Highlight how LiveKit is handling all the complex video processing

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

## Section 5: Advanced Features (3-4 minutes)
- Show the knowledge base integration
  - Show how we've built a simple knowledge system in the backend
  - Explain how the agent retrieves relevant information based on keywords
  - Demonstrate how this makes the agent smarter by providing context
- Show the Langfuse observability integration
  - Walk through the actual Langfuse dashboard (not in our frontend)
  - Show how we've integrated Langfuse in our backend code
  - Explain the metrics and traces it captures
  - Highlight how to use this data for monitoring and optimization
- Emphasize how these additions make your application production-ready

## Section 6: Demo - Technical Support Agent (3-4 minutes)
- Showcase the complete application in a real-world scenario
- Demonstrate the "CloudDash" technical support use case:
  - Share your screen showing a fictional analytics dashboard
  - Ask the agent for help with exporting data
  - Show how the agent can see your screen and provide specific guidance
  - Demonstrate how it references knowledge base information when needed
- Highlight the business benefits:
  - 24/7 visual support without staffing constraints
  - Reduction in repetitive support tickets
  - Improved customer experience through visual guidance
  - Scalable solution for growing companies
- Demonstrate switching between tabs
- Discuss customization options:
  - Different LLMs
  - Custom prompts
  - UI themes
  - Additional plugins

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