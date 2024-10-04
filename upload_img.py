import os
from dotenv import load_dotenv
from imgurpython import ImgurClient
load_dotenv() 

client_id = os.getenv("IMGUR_CLIENT_ID")
client_secret = os.getenv("IMGUR_CLIENT_SECRET")

client = ImgurClient(client_id, client_secret)

# Example request
import requests

url = "https://api.imgur.com/3/image"

payload={'type': 'image',
'title': 'Simple upload',
'description': 'This is a simple image upload in Imgur'}
files=[
  ('image',('GHJQTpX.jpeg',open('qs.jpg','rb'),'image/jpeg'))
]
headers = {
  'Authorization': 'Client-ID {{client_Id}}'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
