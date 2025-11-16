"""Ollama API client."""

import requests
import logging
from typing import List, Dict, Any

from config.settings import get_settings
from exceptions.api import OllamaAPIError

logger = logging.getLogger(__name__)


class OllamaClient:
    """Client for interacting with Ollama API."""
    
    def __init__(self, api_url: str | None = None, model: str | None = None):
        """Initialize Ollama client."""
        settings = get_settings()
        self.api_url = api_url or settings.OLLAMA_API_URL
        self.model = model or settings.DEFAULT_MODEL
    
    def chat(self, messages: List[Dict[str, str]], model: str | None = None) -> str:
        """
        Send chat messages to Ollama API.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Optional model override
        
        Returns:
            Response content from Ollama API
        
        Raises:
            OllamaAPIError: If API call fails
        """
        model = model or self.model
        data = {"model": model, "messages": messages, "stream": False}
        
        try:
            logger.info(f"Sending request to Ollama API with model: {model}")
            response = requests.post(self.api_url, json=data, timeout=120)
            response.raise_for_status()
            
            result = response.json()
            content = result["message"]["content"]
            logger.info("Successfully received response from Ollama API")
            return content
            
        except requests.exceptions.HTTPError as e:
            logger.error(f"Ollama API HTTP error: {e.response.status_code} - {e}")
            raise OllamaAPIError(
                f"API request failed with status {e.response.status_code}: {str(e)}",
                {"api_url": self.api_url, "status_code": e.response.status_code, "error": str(e)}
            )
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Ollama API connection failed: {e}")
            raise OllamaAPIError(
                f"Failed to connect to Ollama. Make sure Ollama is running on {self.api_url}",
                {"api_url": self.api_url, "error": str(e)}
            )
        except requests.exceptions.RequestException as e:
            logger.error(f"Ollama API request failed: {e}")
            raise OllamaAPIError(
                f"Failed to connect to Ollama API: {str(e)}",
                {"api_url": self.api_url, "error": str(e)}
            )
        except KeyError as e:
            logger.error(f"Unexpected response format from Ollama API: {e}")
            raise OllamaAPIError(
                "Unexpected response format from Ollama API",
                {"error": str(e)}
            )
        except Exception as e:
            logger.error(f"Unexpected error calling Ollama API: {e}")
            raise OllamaAPIError(
                f"Unexpected error: {str(e)}",
                {"error": str(e)}
            )

