"""Base intent handler interface."""

from abc import ABC, abstractmethod


class IntentHandler(ABC):
    """Base class for intent handlers."""
    
    @abstractmethod
    def can_handle(self, user_input: str) -> bool:
        """
        Check if this handler can handle the given input.
        
        Args:
            user_input: User's input string
        
        Returns:
            True if this handler can handle the input
        """
        pass
    
    @abstractmethod
    def handle(self, user_input: str) -> str:
        """
        Handle the user input and return a response.
        
        Args:
            user_input: User's input string
        
        Returns:
            Response string
        """
        pass

