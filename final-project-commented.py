#Import importatnt libraries
import gradio as gr
from transformers import pipeline
import ollama

# Load the Whisper model for automatic speech recognition
model_id = "WafaaFraih/whisper-small-egyptian-arabic-All"
pipe = pipeline("automatic-speech-recognition", model=model_id)

# Transcription function
def transcribe_speech(filepath):
    try:
        # Transcribe the audio file
        output = pipe(filepath)
        return output["text"]
    except Exception as e:
        # Return error message if transcription fails
        return f"Error: {str(e)}"

# Format chat history
def format_history(msg: str, history: list[list[str, str]], system_prompt: str):
    # Initialize chat history with system prompt
    chat_history = [{"role": "system", "content": system_prompt}]
    for query, response in history:
        # Append user query and assistant response to chat history
        chat_history.append({"role": "user", "content": query})
        chat_history.append({"role": "assistant", "content": response})  
    # Add the latest user message to chat history
    chat_history.append({"role": "user", "content": msg})
    return chat_history

# Generate response using Ollama's Llama 3.1 model
def generate_response(msg: str, history: list[list[str, str]], system_prompt: str):
    # Format the chat history
    chat_history = format_history(msg, history, system_prompt)
    # Generate response from the model
    response = ollama.chat(model='llama3.1', stream=True, messages=chat_history)
    message = ""
    for partial_resp in response:
        # Concatenate partial responses to form the complete message
        token = partial_resp["message"]["content"]
        message += token
        yield message

# Create Gradio interface
with gr.Blocks() as demo:
    # Inject CSS to make the transcription box RTL for Arabic text
    gr.HTML("""
    <style>
        #transcription_box textarea {
            direction: rtl;
            text-align: right;
        }
    </style>
    """)

    with gr.Row():
        # Transcription section
        with gr.Column():
            gr.Markdown("## Audio Transcription")
            audio_input = gr.Audio(type="filepath", label="Upload Audio File")
            transcription_output = gr.Textbox(label="Transcription", elem_id="transcription_box")
            transcribe_button = gr.Button("Transcribe")
            # Link the transcribe button to the transcribe_speech function
            transcribe_button.click(transcribe_speech, inputs=audio_input, outputs=transcription_output)
        
        # Chatbot section
        with gr.Column():
            gr.Markdown("## Chatbot")
            chatbot = gr.ChatInterface(
                generate_response,
                chatbot=gr.Chatbot(
                    avatar_images=["user.jpg", "chatbot.png"],
                    height="64vh"
                ),
                description="Feel free to ask any question to LLaMA-3.1.",
                theme="soft",
                submit_btn="⬅ Send",
                retry_btn="🔄 Regenerate Response",
                undo_btn="↩ Delete Previous",
                clear_btn="🗑 Clear Chat"
            )

# Launch the interface
demo.launch(debug=True)
