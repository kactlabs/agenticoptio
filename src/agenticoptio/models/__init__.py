"""
Models for AgenticOptio.

This module contains all model implementations and base classes for AgenticOptio.
It provides both abstract base classes for implementing new models and concrete
implementations for popular providers like Ollama.

Available Models:
    - OllamaChat: Local LLM chat using Ollama
    - OllamaEmbedding: Local embeddings using Ollama
    
Base Classes:
    - BaseChatModel: Abstract base for chat model implementations
    - BaseEmbedding: Abstract base for embedding model implementations
    
Utilities:
    - convert_messages: Convert various message formats to API format
    - AIMessage: Response message type with tool call support

Example:
    from agenticoptio.models import OllamaChat, OllamaEmbedding
    
    # Chat model
    chat = OllamaChat(model="llama3.2")
    response = await chat.ainvoke([{"role": "user", "content": "Hello!"}])
    
    # Embedding model  
    embedder = OllamaEmbedding(model="nomic-embed-text")
    vectors = await embedder.aembed(["Hello", "World"])
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