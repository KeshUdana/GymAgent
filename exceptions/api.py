"""API-related exceptions."""

from exceptions.base import GymAgentException


class APIError(GymAgentException):
    """Base exception for API errors."""
    pass


class MistralAPIError(APIError):
    """Exception raised when Mistral API calls fail."""
    pass

