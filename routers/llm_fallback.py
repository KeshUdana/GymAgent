import os
import requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def ask_llm(message: str) -> str:
    """
    Sends message to OpenAI API and returns response.
    Returns error message if API call fails.
    """
    if not OPENAI_API_KEY:
        return "Sorry, the AI service is not configured. Please contact staff directly."

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",  # Fixed: correct model name
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are FitFlow AI, a multilingual gym assistant. "
                    "Use Sinhala/Tamil/English based on user input. "
                    "Be short, friendly, and helpful."
                ),
            },
            {"role": "user", "content": message},
        ],
    }

    try:
        r = requests.post(url, json=data, headers=headers, timeout=10)
        r.raise_for_status()  # Raise exception for bad status codes
        response_data = r.json()
        
        if "choices" in response_data and len(response_data["choices"]) > 0:
            return response_data["choices"][0]["message"]["content"]
        else:
            return "Sorry, I couldn't process that request. Please try again or contact staff."
    except requests.exceptions.RequestException as e:
        print(f"OpenAI API error: {e}")
        return "Sorry, I'm having trouble connecting right now. Please try again later or contact staff."
    except Exception as e:
        print(f"Unexpected error in LLM fallback: {e}")
        return "Sorry, something went wrong. Please contact staff directly."
