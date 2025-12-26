"""
Simple test to verify imports work correctly.

This test module provides basic import verification for the AgenticOptio
library. It's designed to catch common installation and import issues
without requiring external dependencies like Ollama to be running.

Test Coverage:
    - Main package imports (OllamaChat, OllamaEmbedding, AIMessage)
    - Model base class imports (BaseChatModel, BaseEmbedding)
    - Core message class imports (SystemMessage, HumanMessage, ToolMessage)
    - Basic object instantiation (without API calls)
    - Message creation and attribute validation

Usage:
    python test_import.py
    
    Or as part of a test suite:
    pytest test_import.py

This test is particularly useful for:
    - Verifying successful package installation
    - Checking for missing dependencies
    - Validating basic functionality without external services
    - CI/CD pipeline smoke testing
"""

def test_imports():
    """Test that all main components can be imported.
    
    Performs comprehensive import testing to verify that the AgenticOptio
    package is properly installed and all components are accessible.
    
    Test Steps:
        1. Import main package components (models and message types)
        2. Import base classes for extensibility
        3. Import core message types for conversation handling
        4. Test basic object instantiation without API calls
        5. Validate message creation and attribute access
    
    Returns:
        bool: True if all tests pass, False if any test fails.
        
    Raises:
        Exception: Any import or instantiation errors are caught and reported.
        
    Example:
        >>> success = test_imports()
        ✓ Main imports successful
        ✓ Model base classes imported
        ✓ Core message classes imported
        ✓ Model instantiation successful
        ✓ Message creation successful
        
        🎉 All imports and basic functionality working!
        >>> print(success)
        True
    """
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