
from unittest.mock import patch

from src.llm_client import generate_response
import pytest

def test_generate_response_returns_model_text():
    fake_response = {
        "message": {
            "content": "An AI agent can use tools."
        }
    }

    with patch(
        "src.llm_client.ollama.chat",
        return_value=fake_response,
    ) as mock_chat:
        result = generate_response("What is an AI agent?")

    assert result == "An AI agent can use tools."

    mock_chat.assert_called_once_with(
        model="llama3.2:latest",
        messages=[
            {
                "role": "user",
                "content": "What is an AI agent?",
            }
        ],
    )

def test_generate_response_rejects_empty_prompt():
    with pytest.raises(ValueError, match="Prompt cannot be empty"):
        generate_response("")


def test_generate_response_rejects_whitespace_prompt():
    with pytest.raises(ValueError, match="Prompt cannot be empty"):
        generate_response("   ")