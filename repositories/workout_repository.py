"""Repository for workout program data."""

from pathlib import Path
from repositories.base import BaseRepository
from models.workout import WorkoutProgram, WorkoutGoal


class WorkoutRepository(BaseRepository):
    """Repository for accessing workout programs."""
    
    def get_program(self, goal: WorkoutGoal) -> WorkoutProgram:
        """Get workout program for a specific goal."""
        data = self._load_data()
        goal_key = goal.value
        
        if goal_key not in data:
            # Fallback to general_fitness if specific goal not found
            goal_key = WorkoutGoal.GENERAL_FITNESS.value
        
        program_data = data.get(goal_key, {})
        return WorkoutProgram.from_dict(program_data)
    
    def get_all_programs(self) -> dict:
        """Get all workout programs."""
        return self._load_data()

