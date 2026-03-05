# test_model.py

from services.local_llm_service import generate_history_local

story = generate_history_local("A story about a lion, giraffe, and naughty monkey.")
print(story)
