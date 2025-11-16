"""
Translation utility for multilingual responses
Uses LLM to translate English responses to user's language
"""

import os
import requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def translate_response(text: str, target_language: str) -> str:
    """
    Translates English text to target language using LLM.
    Returns original text if translation fails or language is English.
    
    Args:
        text: English text to translate
        target_language: Target language code ("si" for Sinhala, "ta" for Tamil, "en" for English)
    
    Returns:
        Translated text or original text if translation fails
    """
    # No translation needed for English
    if target_language == "en":
        return text
    
    # Map language codes to language names
    language_map = {
        "si": "Sinhala",
        "ta": "Tamil"
    }
    
    target_lang_name = language_map.get(target_language, "English")
    
    if not OPENAI_API_KEY:
        # If no API key, return original text
        return text
    
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Create translation prompt
    prompt = f"""Translate the following gym information text to {target_lang_name}. 
Keep the formatting, emojis, and structure exactly the same. 
Only translate the text content, not the structure or formatting codes.

Text to translate:
{text}

Respond with ONLY the translated text, nothing else."""

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": f"You are a professional translator. Translate gym-related information accurately to {target_lang_name}. Preserve all formatting, emojis, and structure."
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.3,  # Lower temperature for more consistent translations
    }
    
    try:
        r = requests.post(url, json=data, headers=headers, timeout=10)
        r.raise_for_status()
        response_data = r.json()
        
        if "choices" in response_data and len(response_data["choices"]) > 0:
            translated = response_data["choices"][0]["message"]["content"].strip()
            return translated
        else:
            return text  # Return original if translation fails
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # Return original text on error

