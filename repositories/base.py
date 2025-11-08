"""Base repository interface."""

from abc import ABC, abstractmethod
from pathlib import Path
import json
from typing import Dict, Any
import logging

from exceptions.data import DataLoadError, DataNotFoundError

logger = logging.getLogger(__name__)


class BaseRepository(ABC):
    """Base repository for data access."""
    
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self._cache: Dict[str, Any] | None = None
    
    def _load_data(self) -> Dict[str, Any]:
        """Load data from file with caching."""
        if self._cache is not None:
            return self._cache
        
        try:
            if not self.file_path.exists():
                raise DataNotFoundError(
                    f"Data file not found: {self.file_path}",
                    {"file_path": str(self.file_path)}
                )
            
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            self._cache = data
            return data
            
        except json.JSONDecodeError as e:
            raise DataLoadError(
                f"Failed to parse JSON from {self.file_path}",
                {"error": str(e), "file_path": str(self.file_path)}
            )
        except Exception as e:
            raise DataLoadError(
                f"Failed to load data from {self.file_path}",
                {"error": str(e), "file_path": str(self.file_path)}
            )
    
    def clear_cache(self) -> None:
        """Clear the cached data."""
        self._cache = None

