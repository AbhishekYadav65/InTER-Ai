from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env

app = Flask(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["question"]

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_API_KEY}"
        }

        data = {
            "model": "meta-llama/llama-4-scout-17b-16e-instruct",
            "messages": [{"role": "user", "content": user_input}]
        }

        res = requests.post(GROQ_API_URL, headers=headers, json=data)

        if res.status_code == 200:
            response = res.json()["choices"][0]["message"]["content"]
        else:
            response = "Error from Groq API"

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
