"""Service for workout plan operations."""

import logging
from repositories.workout_repository import WorkoutRepository
from clients.mistral_client import MistralClient
from models.workout import WorkoutGoal, WorkoutPlan, WorkoutProgram
from config.settings import get_settings

logger = logging.getLogger(__name__)


class WorkoutService:
    """Service for generating and managing workout plans."""
    
    def __init__(
        self,
        repository: WorkoutRepository | None = None,
        mistral_client: MistralClient | None = None
    ):
        """Initialize workout service."""
        settings = get_settings()
        self.repository = repository or WorkoutRepository(settings.PROGRAM_FILE)
        self.mistral_client = mistral_client or MistralClient()
    
    def _detect_goal(self, user_input: str) -> WorkoutGoal:
        """Detect workout goal from user input."""
        lower = user_input.lower()
        
        if "strength" in lower:
            return WorkoutGoal.STRENGTH
        elif "weight" in lower or "loss" in lower:
            return WorkoutGoal.WEIGHT_LOSS
        else:
            return WorkoutGoal.GENERAL_FITNESS
    
    def generate_workout_plan(self, user_goal: str) -> str:
        """
        Generate a personalized workout plan based on user goal.
        
        Args:
            user_goal: User's workout goal description
        
        Returns:
            Formatted workout plan string
        """
        try:
            # Detect goal from input
            goal = self._detect_goal(user_goal)
            
            # Get base program
            base_program = self.repository.get_program(goal)
            
            # Generate personalized plan with Mistral
            messages = [
                {
                    "role": "system",
                    "content": "You are an expert gym trainer. Create structured, personalized workout plans that are easy to follow."
                },
                {
                    "role": "user",
                    "content": (
                        f"User goal: {user_goal}\n"
                        f"Base plan: {base_program.name} - {base_program.description}\n"
                        f"Exercises: {base_program.exercises}\n"
                        f"Make it personalized and easy to follow."
                    )
                }
            ]
            
            personalized_content = self.mistral_client.chat(messages)
            return personalized_content
            
        except Exception as e:
            logger.error(f"Error generating workout plan: {e}")
            # Check if it's a rate limit error
            if hasattr(e, 'details') and e.details.get('status_code') == 429:
                return "⚠️ I'm receiving too many requests right now. Please wait a moment and try again. Thank you for your patience!"
            elif hasattr(e, 'details') and e.details.get('status_code') == 401:
                return "⚠️ Authentication error. Please contact support."
            else:
                return "⚠️ Sorry, I'm having trouble generating your workout plan right now. Please try again later."

