"""Handler for pricing-related intents."""

from handlers.base import IntentHandler
from services.gym_info_service import GymInfoService


class PricingHandler(IntentHandler):
    """Handler for pricing information requests."""
    
    def __init__(self, gym_info_service: GymInfoService | None = None):
        """Initialize pricing handler."""
        self.gym_info_service = gym_info_service or GymInfoService()
        self.keywords = ["price", "pricing", "membership", "cost", "fee", "fees", "subscription"]
    
    def can_handle(self, user_input: str) -> bool:
        """Check if input is about pricing."""
        lower = user_input.lower()
        return any(keyword in lower for keyword in self.keywords)
    
    def handle(self, user_input: str) -> str:
        """Handle pricing information request."""
        return self.gym_info_service.get_pricing_info()

