"""Handler for workout-related intents."""

from handlers.base import IntentHandler
from services.workout_service import WorkoutService


class WorkoutHandler(IntentHandler):
    """Handler for workout plan requests."""
    
    def __init__(self, workout_service: WorkoutService | None = None):
        """Initialize workout handler."""
        self.workout_service = workout_service or WorkoutService()
        self.keywords = ["workout", "program", "routine", "plan", "exercise", "training"]
    
    def can_handle(self, user_input: str) -> bool:
        """Check if input is about workouts."""
        lower = user_input.lower()
        return any(keyword in lower for keyword in self.keywords)
    
    def handle(self, user_input: str) -> str:
        """Handle workout plan request."""
        return self.workout_service.generate_workout_plan(user_input)

