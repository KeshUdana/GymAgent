"""Mistral API client."""

import requests
import logging
from typing import List, Dict, Any

from config.settings import get_settings
from exceptions.api import MistralAPIError

logger = logging.getLogger(__name__)


class MistralClient:
    """Client for interacting with Mistral API."""
    
    def __init__(self, api_key: str | None = None, api_url: str | None = None, model: str | None = None):
        """Initialize Mistral client."""
        settings = get_settings()
        self.api_key = api_key or settings.MISTRAL_API_KEY
        self.api_url = api_url or settings.MISTRAL_API_URL
        self.model = model or settings.DEFAULT_MODEL
    
    def chat(self, messages: List[Dict[str, str]], model: str | None = None) -> str:
        """
        Send chat messages to Mistral API.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Optional model override
        
        Returns:
            Response content from Mistral API
        
        Raises:
            MistralAPIError: If API call fails
        """
        model = model or self.model
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"model": model, "messages": messages}
        
        try:
            logger.info(f"Sending request to Mistral API with model: {model}")
            response = requests.post(self.api_url, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            logger.info("Successfully received response from Mistral API")
            return content
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Mistral API request failed: {e}")
            raise MistralAPIError(
                f"Failed to connect to Mistral API: {str(e)}",
                {"api_url": self.api_url, "error": str(e)}
            )
        except KeyError as e:
            logger.error(f"Unexpected response format from Mistral API: {e}")
            raise MistralAPIError(
                "Unexpected response format from Mistral API",
                {"error": str(e)}
            )
        except Exception as e:
            logger.error(f"Unexpected error calling Mistral API: {e}")
            raise MistralAPIError(
                f"Unexpected error: {str(e)}",
                {"error": str(e)}
            )

