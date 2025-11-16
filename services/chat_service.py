"""Service for chat operations."""

import logging
from clients.ollama_client import OllamaClient
from models.chat import ChatMessage, MessageRole

logger = logging.getLogger(__name__)


class ChatService:
    """Service for handling general chat interactions."""
    
    def __init__(self, ollama_client: OllamaClient | None = None):
        """Initialize chat service."""
        self.ollama_client = ollama_client or OllamaClient()
    
    def get_general_response(self, user_input: str) -> str:
        """
        Get a general response from the assistant.
        
        Args:
            user_input: User's message
        
        Returns:
            Assistant's response
        """
        try:
            messages = [
                {
                    "role": "system",
                    "content": "You are a friendly and knowledgeable gym assistant. Help users with questions about workouts, gym equipment, fitness tips, and general gym-related inquiries."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
            
            return self.ollama_client.chat(messages)
            
        except Exception as e:
            logger.error(f"Error getting chat response: {e}")
            # Check if it's a rate limit error
            if hasattr(e, 'details') and e.details.get('status_code') == 429:
                return "⚠️ I'm receiving too many requests right now. Please wait a moment and try again. Thank you for your patience!"
            elif hasattr(e, 'details') and e.details.get('status_code') == 401:
                return "⚠️ Authentication error. Please contact support."
            else:
                return "⚠️ Sorry, I'm having trouble connecting to the gym assistant engine right now. Please try again later."

