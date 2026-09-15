# AI Voice Assistant

A Python-based voice assistant that listens to spoken questions, sends them to a local Ollama language model, and responds using voice output.

## Features

- Voice-based user interaction
- Speech recognition using Google Speech Recognition
- Local AI responses using Ollama
- Text-to-speech output using pyttsx3
- Supports multiple questions in one session
- Understands commands such as `stop`, `exit`, `quit`, and `goodbye`
- Conversation memory during the current session
- Audible beep before listening
- Adjustable listening duration

## Technologies Used

- Python
- SpeechRecognition
- Ollama
- Llama 3.2 3B
- pyttsx3
- PyAudio
- winsound

## Requirements

- Python 3.11 or later
- Windows operating system
- Working microphone
- Working speakers
- Ollama installed
- Llama 3.2 model downloaded

## Installation

Clone the repository:

```bash
git clone https://github.com/nithinms2006-dotcom/ai-voice-assistant.git
```

Open the project folder:

```bash
cd ai-voice-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install SpeechRecognition ollama pyttsx3 PyAudio keyboard
```

## Ollama Setup

Install Ollama and download the model:

```bash
ollama pull llama3.2:3b
```

Make sure Ollama is running before starting the assistant.

## Run the Assistant

```bash
python assistant.py
```

The assistant will beep and begin listening for your question.

## Voice Commands

You can say:

- `stop`
- `exit`
- `quit`
- `goodbye`

The assistant will end the session after completing its response.

## Project Structure

```text
ai-voice-assistant/
│
├── assistant.py
├── README.md
└── venv/
```

## Future Improvements

- Wake-word activation
- Better multilingual support
- More natural voices
- Offline speech recognition
- Application and system control
- Web search integration
- GUI interface

## Author

Nithin

## License

This project is for educational and personal use.