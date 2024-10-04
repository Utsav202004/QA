import gradio as gr
import base64
import requests

# Define the function to interact with Together API (Llama 3.2 Vision model)
def llama_chatbot(message, history):
    # Optional: Handle image processing if the user inputs an image in the message
    question = message
    image_file = 'qs.jpg'  # Optional: Replace with image if needed

    # Convert local image to base64 if needed (remove if no image is involved)
    with open(image_file, "rb") as image:
        base64_image = base64.b64encode(image.read()).decode('utf-8')

    # The API endpoint for Together AI
    url = "https://api.together.xyz/v1/chat/completions"

    # Construct the payload to include the user's message and optional image
    payload = {
        "messages": [
            {   "role": "system",
                "content": "Output should always be readable. It should not be in latex or other formats",
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": question
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"  # Include the base64 image string if necessary
                        }
                    }
                ]
            }
        ],
        "model": "meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo"
    }

    # Set your headers (with the correct authorization token)
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer 4bf46a597015a35b5d9daa6e927c35ff500fae6da527e77c0ed95dae23fbfd9c"  # Replace with your API key
    }

    # Send the API request to Together
    response = requests.post(url, json=payload, headers=headers)

    # Extract the content from the API response
    try:
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Error in API request: {str(e)}"

# Create the Gradio Chat Interface for Llama 3.2
gr.ChatInterface(
    llama_chatbot,
    chatbot=gr.Chatbot(height=400),
    textbox=gr.Textbox(placeholder="Ask a question or upload an image", container=False, scale=7),
    title="Llama 3.2 Vision Chatbot",
    description="Ask Llama 3.2 Vision model any question, optionally upload an image for analysis.",
    theme="compact",
    examples=["Hello", "Can you explain this equation?", "Analyze the attached image"],
    cache_examples=True,
    retry_btn="Retry",
    undo_btn="Delete Previous",
    clear_btn="Clear Chat"
).launch()
