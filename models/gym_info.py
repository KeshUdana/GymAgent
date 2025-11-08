"""Gym information data models."""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class ContactInfo:
    """Contact information model."""
    phone: str
    email: str | None = None
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ContactInfo":
        """Create ContactInfo from dictionary."""
        return cls(
            phone=data.get("phone", ""),
            email=data.get("email"),
        )


@dataclass
class PricingInfo:
    """Pricing information model."""
    pricing: Dict[str, str]
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PricingInfo":
        """Create PricingInfo from dictionary."""
        return cls(pricing=data.get("pricing", {}))


@dataclass
class GymInfo:
    """Gym information model."""
    address: str
    hours: str
    contact: ContactInfo
    pricing: PricingInfo
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GymInfo":
        """Create GymInfo from dictionary."""
        return cls(
            address=data.get("address", ""),
            hours=data.get("hours", ""),
            contact=ContactInfo.from_dict(data.get("contact", {})),
            pricing=PricingInfo.from_dict(data),
        )

