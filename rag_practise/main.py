import requests, dotenv
import os
from dotenv import load_dotenv
import time
load_dotenv()

apiKey = os.getenv("GEMINI_API_KEY")

if not apiKey:
    raise ValueError("API key is not Found")

url = (
    "https://generativelanguage.googleapis.com/"
    "v1beta/models/gemini-3.8-flash:generateContent"
)

headers = {
    'content-type' : 'application/json',
    'x-goog-api-key' : apiKey
}






# Store conversation messages
conversation = []

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Chat ended!")
        break

    # Add user message
    conversation.append({
        "role": "user",
        "parts": [
            {"text": question}
        ]
    })

    # Prepare request body
    payload = {
        "contents": conversation
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        result = response.json()

        candidates = result.get("candidates", [])

        if not candidates:
            print("Gemini did not return a response.")
            conversation.pop()
            continue

        parts = candidates[0].get("content", {}).get("parts", [])

        answer = "".join(
            part["text"]
            for part in parts
            if "text" in part
        )

        print("\nGemini:", answer)

        # Store model response
        conversation.append({
            "role": "model",
            "parts": [
                {"text": answer}
            ]
        })

    except requests.exceptions.RequestException as e:
        print("API Error:", e)

        # Remove unanswered user message
        conversation.pop()

