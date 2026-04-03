import os
import requests
from dotenv import load_dotenv
from prompts import PROMPTS

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"


def route_and_respond(message, intent_data):
    intent = intent_data["intent"]

    # Handle unclear intent
    if intent == "unclear":
        return "Please clarify if you need help with coding, data analysis, writing, or career advice."

    # Get the expert prompt
    system_prompt = PROMPTS[intent]

    full_prompt = f"""
{system_prompt}

User question:
{message}
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": full_prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(URL, json=payload)
        data = response.json()

        text = data["candidates"][0]["content"]["parts"][0]["text"]

        return text

    except Exception as e:
        return f"Error generating response: {str(e)}"