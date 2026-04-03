import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"


def classify_intent(message):

    prompt = f"""
Classify the user intent.

Possible intents:
code
data
writing
career
unclear

Return ONLY JSON like this:

{{"intent":"code","confidence":0.92}}

User message: {message}
"""

    payload = {
        "contents":[
            {
                "parts":[{"text":prompt}]
            }
        ]
    }

    try:
        response = requests.post(URL, json=payload, timeout=10)
        data = response.json()

        text = data["candidates"][0]["content"]["parts"][0]["text"]

        # Remove markdown if Gemini returns ```json
        text = text.replace("```json", "").replace("```", "").strip()
        result = json.loads(text)

        intent = result.get("intent", "unclear").strip().lower()
        
        try:
            confidence = float(result.get("confidence", 0.0))
        except:
            confidence = 0.0

        confidence = max(0.0, min(confidence, 1.0))

        # Normalize intent
        if intent in ["programming", "coding", "software"]:
            intent = "code"

        # Confidence threshold
        if confidence < 0.6:
            intent = "unclear"

        # Final validation
        if intent not in ["code", "data", "writing", "career", "unclear"]:
            intent = "unclear"

        return {
            "intent": intent,
            "confidence": confidence
        }
        
    except Exception as e:
        print("Classifier error:", e)
        return {"intent": "unclear", "confidence": 0.0}