import json
import os
from pathlib import Path

def load_json(path: str) -> dict:
    """
    Loads JSON file from given path (relative to project root).
    Returns empty dict if file not found or invalid.
    """
    try:
        full_path = Path(os.getcwd()) / path
        if not full_path.exists():
            print(f"Warning: JSON file not found: {full_path}")
            return {}
        with open(full_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file {path}: {e}")
        return {}
    except Exception as e:
        print(f"Error loading JSON file {path}: {e}")
        return {}
