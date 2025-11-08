"""Service for gym information operations."""

import logging
from repositories.gym_info_repository import GymInfoRepository
from models.gym_info import GymInfo
from config.settings import get_settings

logger = logging.getLogger(__name__)


class GymInfoService:
    """Service for handling gym information requests."""
    
    def __init__(self, repository: GymInfoRepository | None = None):
        """Initialize gym info service."""
        settings = get_settings()
        self.repository = repository or GymInfoRepository(settings.GYM_INFO_FILE)
    
    def get_pricing_info(self) -> str:
        """Get formatted pricing information."""
        try:
            pricing = self.repository.get_pricing()
            if not pricing:
                return "🏷️ **Pricing Info:**\nNo pricing information available."
            
            text = "\n".join([f"- {k}: {v}" for k, v in pricing.items()])
            return f"🏷️ **Pricing Info:**\n{text}"
        except Exception as e:
            logger.error(f"Error getting pricing info: {e}")
            return "⚠️ Sorry, I'm having trouble retrieving pricing information right now."
    
    def get_contact_info(self) -> str:
        """Get formatted contact information."""
        try:
            gym_info = self.repository.get_gym_info()
            contact = gym_info.contact
            
            return (
                f"📍 Address: {gym_info.address}\n"
                f"📞 Phone: {contact.phone}\n"
                f"⏰ Hours: {gym_info.hours}"
            )
        except Exception as e:
            logger.error(f"Error getting contact info: {e}")
            return "⚠️ Sorry, I'm having trouble retrieving contact information right now."
    
    def get_full_info(self) -> GymInfo:
        """Get full gym information."""
        return self.repository.get_gym_info()

