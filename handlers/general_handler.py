"""Handler for general chat intents."""

from handlers.base import IntentHandler
from services.chat_service import ChatService


class GeneralHandler(IntentHandler):
    """Handler for general chat queries (fallback)."""
    
    def __init__(self, chat_service: ChatService | None = None):
        """Initialize general handler."""
        self.chat_service = chat_service or ChatService()
    
    def can_handle(self, user_input: str) -> bool:
        """General handler can always handle input (fallback)."""
        return True
    
    def handle(self, user_input: str) -> str:
        """Handle general chat request."""
        return self.chat_service.get_general_response(user_input)

