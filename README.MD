# AI Voice Assistant

This is a Python-based AI voice assistant project designed to understand user speech, process requests using artificial intelligence, and respond naturally through voice.

## About the Project

I am building an AI voice assistant that can listen to what the user says, understand the request, generate an intelligent response, and communicate the answer using voice.

The main goal of this project is to create a simple and natural voice assistant that allows users to communicate in their own language, similar to how we interact with assistants such as Siri and Google Assistant.

The assistant is being developed with a focus on real-time voice interaction, AI-powered responses, conversation context, and future multilingual support.

## Current Progress

### Completed

* Project structure created
* Python virtual environment configured
* Required Python libraries installed
* Basic speech recognition implemented
* Basic text-to-speech implemented
* Continuous listening loop implemented
* Basic error handling added
* GitHub repository created
* Git version control configured
* Ollama installed as a local AI backend
* Llama 3.2 3B model downloaded and configured
* Python connected to Ollama
* AI responses successfully generated using Llama 3.2 3B
* Speech recognition connected with Ollama
* User voice converted into text and sent to the AI model
* AI responses converted into speech
* Continuous voice conversation implemented
* Voice assistant optimized to provide shorter and faster responses
* Conversation memory implemented
* Follow-up questions supported using previous conversation context
* Listening time increased to allow longer voice commands

## Next Steps

* Improve conversation speed and responsiveness
* Improve speech recognition accuracy
* Improve voice response quality
* Add multilingual speech recognition
* Make the assistant respond in the same language as the user
* Improve natural conversation
* Add voice commands and useful assistant features
* Add more advanced AI capabilities
* Improve interruption and stop-speaking functionality
* Add additional AI tools and integrations

## Technologies Used

* Python
* SpeechRecognition
* PyAudio
* pyttsx3
* Ollama
* Llama 3.2 3B
* python-dotenv
* Git
* GitHub

## Project Architecture

```text
User speaks
     ↓
Microphone
     ↓
Speech Recognition
     ↓
Text temporarily stored in memory
     ↓
Conversation History
     ↓
Ollama + Llama 3.2 3B
     ↓
AI-generated response
     ↓
Conversation History Updated
     ↓
Text-to-Speech
     ↓
Voice response
```

## Conversation Memory

The assistant maintains the current conversation context in memory.

This allows follow-up questions to use information from previous questions.

For example:

```text
User: Who is Virat Kohli?
Assistant: Virat Kohli is an Indian cricketer...

User: How old is he?
Assistant: ...
```

The previous conversation is provided to the AI model so that follow-up questions can be understood in context.

## Privacy

The recognized speech is processed temporarily in memory and is not intentionally saved as `.txt` files by the application.

The current speech recognition implementation uses Google's speech recognition service through the SpeechRecognition library, while the AI response generation is handled locally using Ollama.

## Future Goal

The long-term goal of this project is to develop a powerful multilingual AI voice assistant that can understand natural speech, maintain natural conversations, communicate in different languages, perform useful tasks, and provide a smooth real-time conversational experience.
