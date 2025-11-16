# flow_manager.py
import json
from pathlib import Path
from typing import Dict, Any

class FlowManager:
    def __init__(self, language: str):
        self.language = language
        self.flow_data = self.load_flow(language)

    def load_flow(self, lang: str) -> Dict[str, Any]:
        # flows directory is at project root, not in routers/
        base_path = Path(__file__).parent.parent / "flows"
        file_path = base_path / f"{lang}.json"

        if not file_path.exists():
            # Fallback to English if language file doesn't exist
            file_path = base_path / "en.json"
            if not file_path.exists():
                # Return empty structure if no files exist
                return {"welcome": "Welcome!", "intents": {}}

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading flow file {file_path}: {e}")
            return {"welcome": "Welcome!", "intents": {}}

    def get_welcome(self) -> str:
        return self.flow_data.get("welcome", "")

    def match_intent(self, user_message: str) -> str:
        user_message = user_message.lower()

        # Check if intents key exists
        intents = self.flow_data.get("intents", {})
        if not intents:
            return "I'm not sure I understand. Can you rephrase?"

        for _, intent_data in intents.items():
            patterns = intent_data.get("patterns", [])
            for pattern in patterns:
                # Use simple string matching (case-insensitive) for safety
                # Patterns in JSON are treated as literal strings, not regex
                if pattern.lower() in user_message:
                    return intent_data.get("response", "I'm not sure I understand. Can you rephrase?")

        # fallback
        return "I'm not sure I understand. Can you rephrase?"

    def get_response(self, user_message: str) -> str:
        # 1st message welcome
        if user_message.lower() in ["hi", "hello", "hey"]:
            return self.get_welcome()

        return self.match_intent(user_message)
