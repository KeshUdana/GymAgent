"""Data repositories for accessing stored data."""

from repositories.gym_info_repository import GymInfoRepository
from repositories.workout_repository import WorkoutRepository

__all__ = [
    "GymInfoRepository",
    "WorkoutRepository",
]

