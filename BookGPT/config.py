# config.py

import os
from dotenv import load_dotenv

load_dotenv()

# --- OpenAI ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1500))

# --- App Defaults ---
APP_TITLE = "AI History Explorer"

DEFAULT_DEPTH = "Standard"
DEFAULT_AUDIENCE = "Adult"
DEFAULT_NARRATION = "Neutral"