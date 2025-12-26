"""
Streaming example for AgenticOptio OllamaChat.

This example demonstrates real-time streaming capabilities of OllamaChat,
which is essential for interactive applications where users want to see
responses as they are generated rather than waiting for completion.

Features demonstrated:
1. Streaming response initialization and setup
2. Real-time token processing and display
3. Proper async iteration over streaming responses
4. Console output formatting for smooth user experience

Prerequisites:
    - Ollama running locally with streaming support enabled
    - Model installed that supports streaming (most modern models do)
    - Terminal that supports real-time output flushing

Usage:
    python examples/streaming_example.py

Benefits of Streaming:
    - Improved user experience with immediate feedback
    - Lower perceived latency for long responses
    - Ability to process tokens as they arrive
    - Better interactivity for chat applications
"""

import asyncio
from agenticoptio import OllamaChat


async def main():
    """Demonstrate streaming response capabilities.
    
    This function showcases the streaming API by:
    - Setting up a streaming-capable OllamaChat instance
    - Sending a request that will generate a substantial response
    - Processing and displaying tokens in real-time as they arrive
    - Properly handling the async iteration over response chunks
    
    The example uses a creative writing prompt to generate enough content
    to demonstrate the streaming effect clearly. Each token is displayed
    immediately as it's received from the model.
    """
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