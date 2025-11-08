"""Service for chat operations."""

import logging
from clients.mistral_client import MistralClient
from models.chat import ChatMessage, MessageRole

logger = logging.getLogger(__name__)


class ChatService:
    """Service for handling general chat interactions."""
    
    def __init__(self, mistral_client: MistralClient | None = None):
        """Initialize chat service."""
        self.mistral_client = mistral_client or MistralClient()
    
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
            
            return self.mistral_client.chat(messages)
            
        except Exception as e:
            logger.error(f"Error getting chat response: {e}")
            return "⚠️ Sorry, I'm having trouble connecting to the gym assistant engine right now. Please try again later."

