"""
AgenticOptio - Disciplined AI agent coordination library.

Named after the Roman Optio, this framework brings military-grade coordination,
resilience, and execution discipline to multi-model AI operations.

Currently supports Ollama with OpenAI, Anthropic, and other providers coming soon.
"""

from agenticoptio.models.ollama import OllamaChat, OllamaEmbedding
from agenticoptio.models.base import AIMessage, BaseChatModel, BaseEmbedding

__version__ = "0.1.1"

__all__ = [
    "OllamaChat",
    "OllamaEmbedding", 
    "AIMessage",
    "BaseChatModel",
    "BaseEmbedding",
]