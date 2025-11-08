import os

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "your_mistral_api_key_here")
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

DEFAULT_MODEL = "mistral-large-latest"

# Streamlit app settings
APP_TITLE = "GymX Assistant"
