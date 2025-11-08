import requests
from config.settings import MISTRAL_API_KEY, MISTRAL_API_URL, DEFAULT_MODEL

def query_mistral(messages, model=DEFAULT_MODEL):
    headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}"}
    data = {"model": model, "messages": messages}
    
    try:
        response = requests.post(MISTRAL_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print("Error contacting Mistral:", e)
        return "⚠️ Sorry, I'm having trouble connecting to the gym assistant engine right now."
