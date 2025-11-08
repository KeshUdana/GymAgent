"""Intent router for directing queries to appropriate handlers."""

import logging
from typing import List
from handlers.base import IntentHandler
from handlers.workout_handler import WorkoutHandler
from handlers.pricing_handler import PricingHandler
from handlers.contact_handler import ContactHandler
from handlers.general_handler import GeneralHandler

logger = logging.getLogger(__name__)


class IntentRouter:
    """Routes user intents to appropriate handlers."""
    
    def __init__(self, handlers: List[IntentHandler] | None = None):
        """
        Initialize intent router.
        
        Args:
            handlers: Optional list of custom handlers. If None, uses default handlers.
        """
        if handlers is None:
            # Initialize default handlers in priority order
            self.handlers = [
                WorkoutHandler(),
                PricingHandler(),
                ContactHandler(),
                GeneralHandler(),  # Fallback handler (always returns True)
            ]
        else:
            self.handlers = handlers
    
    def route(self, user_input: str) -> str:
        """
        Route user input to appropriate handler.
        
        Args:
            user_input: User's input string
        
        Returns:
            Response from the appropriate handler
        """
        if not user_input or not user_input.strip():
            return "Please provide a question or request."
        
        # Find the first handler that can handle this input
        for handler in self.handlers:
            try:
                if handler.can_handle(user_input):
                    logger.info(f"Routing to {handler.__class__.__name__} for input: {user_input[:50]}")
                    return handler.handle(user_input)
            except Exception as e:
                logger.error(f"Error in handler {handler.__class__.__name__}: {e}")
                # Continue to next handler on error
                continue
        
        # Fallback response (should never reach here if GeneralHandler is included)
        return "I'm sorry, I couldn't process your request. Please try rephrasing your question."

