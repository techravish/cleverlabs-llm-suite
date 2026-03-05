from services.local_llm_service import generate_history_local

def generate_history(description: str) -> str:
    prompt = f"Generate a short story based on: {description}"
    return generate_history_local(prompt)