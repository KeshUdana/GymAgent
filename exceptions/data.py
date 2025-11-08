"""Data-related exceptions."""

from exceptions.base import GymAgentException


class DataLoadError(GymAgentException):
    """Exception raised when data cannot be loaded."""
    pass


class DataNotFoundError(GymAgentException):
    """Exception raised when requested data is not found."""
    pass

