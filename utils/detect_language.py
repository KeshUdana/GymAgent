# language_detector.py
import re

class LanguageDetector:
    @staticmethod
    def detect(text: str) -> str:
        text = text.strip()

        # Sinhala Unicode block
        if re.search(r'[\u0D80-\u0DFF]', text):
            return "si"

        # Tamil Unicode block
        if re.search(r'[\u0B80-\u0BFF]', text):
            return "ta"

        # Default → English
        return "en"
