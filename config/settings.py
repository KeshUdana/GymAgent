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
        
        # Ollama API settings
        self.OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/chat")
        self.DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
        
        # Application settings
        self.APP_TITLE = "GymX Assistant"
        self.APP_DESCRIPTION = "💬 Your personalized gym assistant powered by Ollama"
        
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

