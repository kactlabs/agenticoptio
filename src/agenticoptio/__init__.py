"""
AgenticOptio - Lightweight AI agent library supporting multiple model providers.

Currently supports Ollama with OpenAI, Anthropic, and other providers coming soon.
"""

from agenticoptio.models.ollama import OllamaChat, OllamaEmbedding
from agenticoptio.models.base import AIMessage, BaseChatModel, BaseEmbedding

__version__ = "0.1.0"

__all__ = [
    "OllamaChat",
    "OllamaEmbedding", 
    "AIMessage",
    "BaseChatModel",
    "BaseEmbedding",
]