# Audio Transcription and Chatbot Web App

## Overview
This web app integrates the Whisper model for automatic speech recognition (ASR) and Ollama’s Llama 3.1 for chatbot functionality. Users can upload an audio file, transcribe its speech to text, and interact with a chatbot to perform any further task such as summarization or extracting any information from the audio. The app is built using Gradio and leverages Python, Hugging Face’s Transformers library, Ollama API, and Gradio for creating interactive interfaces.

## Features
- **Audio Transcription**: Users can upload audio files (preferably in a supported format) to transcribe speech into text.
- **Chatbot Interaction**: Users can converse with a chatbot powered by Llama 3.1, providing responses based on their input.
- **RTL Support**: The transcription box is designed to support right-to-left (RTL) text direction for languages like Arabic.
- **Interactive UI**: The app has an intuitive and user-friendly interface built with Gradio.

## Installation
1. Clone the repository.
2. Install the required Python packages and run the app using:
   ```bash
   pip install -r requirements.txt
   python final-project-commented.py


## Usage
1. **Open the app in your browser.**
2. **Audio Transcription:**
   - Upload an audio file using the “Upload Audio File” button.
   - Click on the "Transcribe" button to start the transcription.
   - The transcribed text will appear in the "Transcription" box.
3. **Chatbot:**
   - Use the chat interface to interact with the chatbot powered by Llama 3.1.
   - Ask questions or have a conversation with the model.


## Acknowledgments
- **Whisper Model** by OpenAI: Used for automatic speech recognition. You can learn more on the [Whisper GitHub page](https://github.com/openai/whisper).
- **Llama 3.1** by Ollama: A large language model for chat responses. Learn more about Ollama's models [here](https://ollama.com/).
- **Gradio**: An easy-to-use Python library for creating interactive web interfaces. Visit the [Gradio Documentation](https://gradio.app/) for more details.
- **Hugging Face Transformers**: The `pipeline` function is used to load models for automatic speech recognition.

## Contributers
[Asmaa Yaser](https://github.com/AsmaaYaser26)

[Wafaa Abdullah](https://github.com/Wafaa-Abdullah)

[Mona ElAhabrawy]()


