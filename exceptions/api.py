"""API-related exceptions."""

from exceptions.base import GymAgentException


class APIError(GymAgentException):
    """Base exception for API errors."""
    pass


class MistralAPIError(APIError):
    """Exception raised when Mistral API calls fail."""
    pass


class OllamaAPIError(APIError):
    """Exception raised when Ollama API calls fail."""
    pass
