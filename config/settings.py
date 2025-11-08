"""Application settings and configuration."""

import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """Application settings singleton."""
    
    _instance: Optional["Settings"] = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        # Mistral API settings
        self.MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "your_mistral_api_key_here")
        self.MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"
        self.DEFAULT_MODEL = "mistral-large-latest"
        
        # Application settings
        self.APP_TITLE = "GymX Assistant"
        self.APP_DESCRIPTION = "💬 Your personalized gym assistant powered by Mistral"
        
        # Paths
        self.BASE_DIR = Path(__file__).parent.parent
        self.DATA_DIR = self.BASE_DIR / "data"
        self.LOGS_DIR = self.BASE_DIR / "logs"
        
        # Data files
        self.GYM_INFO_FILE = self.DATA_DIR / "gym.info.json"
        self.PROGRAM_FILE = self.DATA_DIR / "program.json"
        
        # Logging
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
        self.LOG_FILE = self.LOGS_DIR / "logs.txt"
        
        self._initialized = True
    
    def validate(self) -> bool:
        """Validate settings."""
        if not self.DATA_DIR.exists():
            self.DATA_DIR.mkdir(parents=True, exist_ok=True)
        if not self.LOGS_DIR.exists():
            self.LOGS_DIR.mkdir(parents=True, exist_ok=True)
        return True


def get_settings() -> Settings:
    """Get settings instance."""
    settings = Settings()
    settings.validate()
    return settings

