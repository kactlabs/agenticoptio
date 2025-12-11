"""
Models for AgenticOptio.

Contains OllamaChat and OllamaEmbedding models with their base classes.
"""

from agenticoptio.models.base import AIMessage, BaseChatModel, BaseEmbedding, convert_messages
from agenticoptio.models.ollama import OllamaChat, OllamaEmbedding

__all__ = [
    "AIMessage",
    "BaseChatModel", 
    "BaseEmbedding",
    "convert_messages",
    "OllamaChat",
    "OllamaEmbedding",
]