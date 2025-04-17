import requests
import json
import os
from dotenv import load_dotenv

# Load Groq API key from .env
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

# Define the endpoint
url = "https://api.groq.com/openai/v1/chat/completions"

# Set up headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Define the payload
data = {
    "model": "meta-llama/llama-4-scout-17b-16e-instruct",
    "messages": [
        {"role": "user", "content": "Explain the importance of fast language models"}
    ]
}

# Make the request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response
if response.status_code == 200:
    result = response.json()
    print("Response:", result)
else:
    print("Error:", response.status_code, response.text)
