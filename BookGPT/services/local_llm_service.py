from llama_cpp import Llama

# Load model once at startup
model = Llama(model_path="models/llama-3.2-1b-instruct-q8_0.gguf")

def generate_history_local(prompt: str, max_tokens: int = 2000) -> str:
    output = model(prompt, max_tokens=max_tokens)
    return output['choices'][0]['text']