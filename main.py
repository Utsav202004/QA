import requests

url = "https://api.together.xyz/v1/chat/completions"

# Use the image URL you uploaded to an external service
image_url = "https://drive.google.com/uc?export=download&id=1IAJabe6o8_bRZyDX1pUoDFVUNQtXSh9w"
 # Replace with your actual image URL

# Payload with only user messages and no system message
payload = {
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Differentiate each function in the given image step-by-step as per CBSE board standards"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                }
            ]
        }
    ],
    "model": "meta-llama/Llama-Vision-Free"
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer 4bf46a597015a35b5d9daa6e927c35ff500fae6da527e77c0ed95dae23fbfd9c"
}

# Send the request
response = requests.post(url, json=payload, headers=headers)
print("Done")
# Print the response
print(response.json()['choices'][0]['message']['content'])

