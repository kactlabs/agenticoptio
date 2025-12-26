"""
Basic usage example for AgenticOptio OllamaChat.

This example demonstrates the fundamental usage patterns of OllamaChat
for conversational AI applications. It shows how to:

1. Initialize an OllamaChat instance
2. Send messages and receive responses
3. Maintain conversation context across multiple exchanges
4. Handle asynchronous operations properly

Prerequisites:
    - Ollama must be running locally (default: http://localhost:11434)
    - The specified model must be installed (e.g., `ollama pull llama3.2`)
    - AgenticOptio must be installed with OpenAI dependency

Usage:
    python examples/basic_usage.py

Note:
    This example uses llama3.2 by default. Change the model parameter
    to use a different model that you have installed in Ollama.
"""

import asyncio
from agenticoptio import OllamaChat


async def main():
    """Demonstrate basic OllamaChat usage with conversation flow.
    
    This function shows a complete conversation example including:
    - Model initialization with specific model selection
    - Single message exchange with response handling
    - Multi-turn conversation with context preservation
    - Proper async/await patterns for non-blocking operations
    
    The example simulates a natural conversation flow where the user
    asks about a topic and then follows up with related questions,
    demonstrating how to maintain conversation context.
    """
    # Create an OllamaChat instance
    llm = OllamaChat(model="llama3.2")  # Make sure this model is installed in Ollama
    
    # Simple conversation
    messages = [
        {"role": "user", "content": "Hello! What's the capital of Canada?"}
    ]
    
    print("Sending message to Ollama...")
    response = await llm.ainvoke(messages)
    print(f"Response: {response.content}")
    
    # Continue the conversation
    messages.append({"role": "assistant", "content": response.content})
    messages.append({"role": "user", "content": "What's the population of that city?"})
    
    print("\nSending follow-up message...")
    response = await llm.ainvoke(messages)
    print(f"Response: {response.content}")


if __name__ == "__main__":
    asyncio.run(main())