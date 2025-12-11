"""
Basic usage example for AgenticOptio OllamaChat.

This example shows how to use OllamaChat for simple conversations.
Make sure you have Ollama running locally with a model installed.
"""

import asyncio
from agenticoptio import OllamaChat


async def main():
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