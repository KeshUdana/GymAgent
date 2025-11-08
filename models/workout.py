"""Workout-related data models."""

from dataclasses import dataclass
from typing import Dict, Any, List
from enum import Enum


class WorkoutGoal(str, Enum):
    """Workout goal types."""
    STRENGTH = "strength"
    WEIGHT_LOSS = "weight_loss"
    GENERAL_FITNESS = "general_fitness"


@dataclass
class WorkoutProgram:
    """Base workout program model."""
    name: str
    description: str
    exercises: List[Dict[str, Any]]
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "WorkoutProgram":
        """Create WorkoutProgram from dictionary."""
        return cls(
            name=data.get("name", ""),
            description=data.get("description", ""),
            exercises=data.get("exercises", []),
        )


@dataclass
class WorkoutPlan:
    """Personalized workout plan model."""
    goal: WorkoutGoal
    base_program: WorkoutProgram
    personalized_content: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert WorkoutPlan to dictionary."""
        return {
            "goal": self.goal.value,
            "base_program": {
                "name": self.base_program.name,
                "description": self.base_program.description,
                "exercises": self.base_program.exercises,
            },
            "personalized_content": self.personalized_content,
        }

