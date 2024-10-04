import base64
import requests

# Path to the local image
image_file = 'qs.jpg'  # Replace with your local image path

# Read the image file and encode it in base64
with open(image_file, "rb") as image:
    base64_image = base64.b64encode(image.read()).decode('utf-8')

# The API endpoint
url = "https://api.together.xyz/v1/chat/completions"

# Construct the payload to include the base64 image data
payload = {
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "differentiate each equation that you find in the image step-by-step with full explanation for each step"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"  # Embedded base64 image string
                    }
                }
            ]
        }
    ],
    "model": "meta-llama/Llama-Vision-Free"
}

# Set your headers (ensure you have the right authorization token)
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer 4bf46a597015a35b5d9daa6e927c35ff500fae6da527e77c0ed95dae23fbfd9c"  # Replace with your API key
}

# Send the API request
response = requests.post(url, json=payload, headers=headers)

# Print the response
print(response.json()['choices'][0]['message']['content'])
