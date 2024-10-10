import gradio as gr
import base64
import requests
from PIL import Image
import os

# Directory to save uploaded images
save_dir = "images"

# Create the directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Path to save the uploaded image
save_path = os.path.join(save_dir, "uploaded_img.png")

def save_image(image: Image.Image, save_path: str):
    if image:
        image.save(save_path)
    else:
        print("No image to save.")

def llama_chatbot(image, message, history):
    save_image(image, save_path)
    question = message
    
    if image:
        with open(save_path, "rb") as img_file:
            base64_image = base64.b64encode(img_file.read()).decode('utf-8')
    else:
        base64_image = ""
    
    url = "https://api.together.xyz/v1/chat/completions"

    payload = {
        "messages": [
            {
                "role": "system",
                "content": "Output should always be readable. It should not be in LaTeX or other formats."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": question
                    }
                ]
            }
        ],
        "model": "meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo"
    }
    
    if base64_image:
        payload["messages"][1]["content"].append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
        })
    
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer 4bf46a597015a35b5d9daa6e927c35ff500fae6da527e77c0ed95dae23fbfd9c"  # Replace with your actual API key
    }

    response = requests.post(url, json=payload, headers=headers)
    


    try:
        content = response.json()['choices'][0]['message']['content']
        history = history or []
        history.append(("User", message))
        history.append(("Bot", content))
        return history, history
    except Exception as e:
        return history, history + [("Bot", f"Error in API request: {str(e)}")]

def clear_chat():
    return [], []
