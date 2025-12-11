"""
Simple test to verify imports work correctly.
"""

def test_imports():
    """Test that all main components can be imported."""
    try:
        # Test main imports
        from agenticoptio import OllamaChat, OllamaEmbedding, AIMessage
        print("✓ Main imports successful")
        
        # Test model imports
        from agenticoptio.models import BaseChatModel, BaseEmbedding
        print("✓ Model base classes imported")
        
        # Test core imports
        from agenticoptio.core.messages import SystemMessage, HumanMessage, ToolMessage
        print("✓ Core message classes imported")
        
        # Test instantiation (without calling Ollama)
        chat = OllamaChat(model="llama3.2")
        embedding = OllamaEmbedding(model="nomic-embed-text")
        print("✓ Model instantiation successful")
        
        # Test message creation
        msg = AIMessage("Hello world")
        assert msg.content == "Hello world"
        assert msg.role == "assistant"
        print("✓ Message creation successful")
        
        print("\n🎉 All imports and basic functionality working!")
        return True
        
    except Exception as e:
        print(f"❌ Import test failed: {e}")
        return False


if __name__ == "__main__":
    test_imports()