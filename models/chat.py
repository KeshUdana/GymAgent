"""Chat-related data models."""

from dataclasses import dataclass
from typing import List, Literal
from enum import Enum


class MessageRole(str, Enum):
    """Chat message role types."""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


@dataclass
class ChatMessage:
    """Chat message model."""
    role: MessageRole
    content: str
    
    def to_dict(self) -> dict:
        """Convert ChatMessage to dictionary."""
        return {
            "role": self.role.value,
            "content": self.content,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "ChatMessage":
        """Create ChatMessage from dictionary."""
        return cls(
            role=MessageRole(data.get("role", "user")),
            content=data.get("content", ""),
        )


@dataclass
class ChatHistory:
    """Chat history container."""
    messages: List[ChatMessage]
    
    def add_message(self, message: ChatMessage) -> None:
        """Add a message to the history."""
        self.messages.append(message)
    
    def get_messages_dict(self) -> List[dict]:
        """Get messages as list of dictionaries."""
        return [msg.to_dict() for msg in self.messages]
    
    def clear(self) -> None:
        """Clear all messages."""
        self.messages.clear()

