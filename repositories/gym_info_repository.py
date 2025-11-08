"""Repository for gym information data."""

from pathlib import Path
from repositories.base import BaseRepository
from models.gym_info import GymInfo


class GymInfoRepository(BaseRepository):
    """Repository for accessing gym information."""
    
    def get_gym_info(self) -> GymInfo:
        """Get gym information."""
        data = self._load_data()
        return GymInfo.from_dict(data)
    
    def get_pricing(self) -> dict:
        """Get pricing information."""
        data = self._load_data()
        return data.get("pricing", {})
    
    def get_contact(self) -> dict:
        """Get contact information."""
        data = self._load_data()
        return data.get("contact", {})

