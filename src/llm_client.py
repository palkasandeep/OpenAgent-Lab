
import ollama

MODEL_NAME = "llama3.2:latest"


import ollama

from src.config import MODEL_NAME


def generate_response(prompt: str) -> str:
    """Generate a response using a locally running Ollama model."""
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]


if __name__ == "__main__":
    answer = generate_response(
        "Explain what an AI agent is in three sentences."
    )
    print(answer)

def generate_response(prompt: str) -> str:
    """Generate a response using a locally running Ollama model."""
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return response["message"]["content"]


if __name__ == "__main__":
    answer = generate_response(
        "Explain what an AI agent is in three sentences."
    )
    print(answer)
