import gradio as gr
from utilis import llama_chatbot, clear_chat


with gr.Blocks() as demo:
    gr.Markdown("<h1>Maths Doubt Solver</h1>")
    
    with gr.Row():
        with gr.Column(scale=1):
            image_input = gr.Image(type="pil", label="Upload an Image")
            text_input = gr.Textbox(label="Ask your math question", placeholder="Type your question here...")
            submit_btn = gr.Button("Submit")
            clear_btn = gr.Button("Clear Chat")
    
        with gr.Column(scale=2):
            chatbot = gr.Chatbot(label="Chat History", height=700)
    
    submit_btn.click(fn=llama_chatbot, inputs=[image_input, text_input, chatbot], outputs=[chatbot, chatbot])
    clear_btn.click(fn=clear_chat, inputs=None, outputs=chatbot)

demo.launch()
