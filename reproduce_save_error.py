import requests
import json

url = "http://localhost:5000/api/save"

payload = {
    "raw_content": "Test content",
    "context": "Test context",
    "tone": "Neutral",
    "analysis": {
        "scene_tag": "Test Scene",
        "intent_tag": "Test Intent",
        "polished_text": "Polished test content",
        "explanation": "Test explanation",
        "key_phrases": ["test", "content"]
    }
}

try:
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Request failed: {e}")
