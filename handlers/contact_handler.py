"""Handler for contact-related intents."""

from handlers.base import IntentHandler
from services.gym_info_service import GymInfoService


class ContactHandler(IntentHandler):
    """Handler for contact information requests."""
    
    def __init__(self, gym_info_service: GymInfoService | None = None):
        """Initialize contact handler."""
        self.gym_info_service = gym_info_service or GymInfoService()
        self.keywords = ["contact", "location", "address", "time", "hours", "phone", "where", "when"]
    
    def can_handle(self, user_input: str) -> bool:
        """Check if input is about contact information."""
        lower = user_input.lower()
        return any(keyword in lower for keyword in self.keywords)
    
    def handle(self, user_input: str) -> str:
        """Handle contact information request."""
        return self.gym_info_service.get_contact_info()

