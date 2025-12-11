"""
Streaming example for AgenticOptio OllamaChat.

This example shows how to use streaming responses with OllamaChat.
"""

import asyncio
from agenticoptio import OllamaChat


async def main():
    # Create an OllamaChat instance
    llm = OllamaChat(model="llama3.2")
    
    # Message to stream
    messages = [
        {"role": "user", "content": "Write a short story about a robot learning to paint."}
    ]
    
    print("Streaming response from Ollama...")
    print("Response: ", end="", flush=True)
    
    # Stream the response
    async for chunk in llm.astream(messages):
        print(chunk.content, end="", flush=True)
    
    print("\n\nStreaming complete!")


if __name__ == "__main__":
    asyncio.run(main())