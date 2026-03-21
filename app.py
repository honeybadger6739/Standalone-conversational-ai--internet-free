import gradio as gr
import requests

def chat_with_ai(user_input):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": user_input,
            "stream": False
        }
    )
    
    return response.json()["response"]

# UI create chestunnam
app = gr.Interface(
    fn=chat_with_ai,   # AI function
    inputs=gr.Textbox(label="Enter your question"),
    outputs=gr.Textbox(label="AI Response"),
    title="Offline AI Assistant",
    description="Runs locally using Ollama"
)

app.launch()