"""
Core components for AgenticOptio.

This module provides the core message types and base classes used throughout
the AgenticOptio library. It serves as the central import point for fundamental
components like message classes and base model interfaces.

The core module includes:
    - Message types (AIMessage, SystemMessage, HumanMessage, ToolMessage)
    - Base message functionality and serialization
    - Common interfaces for chat and embedding models

Example:
    from agenticoptio.core import AIMessage, SystemMessage
    
    system_msg = SystemMessage("You are a helpful assistant")
    ai_response = AIMessage("Hello! How can I help you?")
"""

from agenticoptio.core.messages import AIMessage, BaseMessage, SystemMessage, HumanMessage, ToolMessage

__all__ = [
    "AIMessage",
    "BaseMessage", 
    "SystemMessage",
    "HumanMessage",
    "ToolMessage",
]