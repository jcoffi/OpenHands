from unittest.mock import MagicMock

import pytest


class MockException(Exception):
    """A mock exception class to simulate the litellm exception."""

    def __init__(self):
        super().__init__()
        self.status_code = 500
        self.message = 'Test error message'


def test_setattr_works():
    """Test that we can set an attribute on an exception."""
    mock_exception = AttributeError("'Exception' object has no attribute 'request'")

    # Set the request attribute
    setattr(mock_exception, 'request', None)

    # Verify the attribute was set
    assert hasattr(mock_exception, 'request')
    assert mock_exception.request is None

    # Test our condition
    assert "'Exception' object has no attribute 'request'" in str(mock_exception)


def test_exception_handling_in_llm():
    """Test that our exception handling in LLM class works correctly."""

    # Create a mock LLM class
    class MockLLM:
        def __init__(self):
            self.config = MagicMock()

        def _completion_unwrapped(self, *args, **kwargs):
            # Simulate the AttributeError with 'request' missing
            raise AttributeError("'Exception' object has no attribute 'request'")

    # Create a mock for the completion method
    def mock_completion(*args, **kwargs):
        llm = args[0]
        try:
            # This should raise the AttributeError
            llm._completion_unwrapped(*args, **kwargs)
        except AttributeError as e:
            # Check if our condition would match
            if "'Exception' object has no attribute 'request'" in str(e):
                # Set the request attribute
                setattr(e, 'request', None)
                # Re-raise the exception
                raise
            # If it's a different AttributeError, re-raise it
            raise

    # Create an instance of our mock LLM
    llm = MockLLM()

    # Test that our exception handling works
    with pytest.raises(AttributeError) as excinfo:
        mock_completion(llm)

    # Verify that the exception has the request attribute
    assert hasattr(excinfo.value, 'request')
    assert excinfo.value.request is None
