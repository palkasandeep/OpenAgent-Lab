
import ollama
import httpx


from src.config import MODEL_NAME


def generate_response(prompt: str) -> str:
    """Generate a response using a locally running Ollama model."""

    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
    except httpx.ConnectError as exc:
        raise RuntimeError(
            "Cannot connect to Ollama. Check whether Ollama is running."
        ) from exc

    return response["message"]["content"]



if __name__ == "__main__":
    answer = generate_response(
        "Explain what an AI agent is in three sentences."
    )
    print(answer)
