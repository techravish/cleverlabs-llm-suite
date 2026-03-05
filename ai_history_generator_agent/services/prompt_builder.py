def build_prompt(place, depth, audience, narration_mode):
    depth_map = {
        "Quick": "Provide a concise summary (200 words).",
        "Standard": "Provide a detailed summary (500 words).",
        "Deep Dive": "Provide a comprehensive historical analysis (1000+ words)."
    }

    audience_map = {
        "Adult": "Use clear and engaging language suitable for general adults.",
        "Kid": "Explain in very simple, fun language suitable for a 10-year-old.",
        "Academic": "Use formal academic tone with historical precision."
    }

    narration_map = {
        "Neutral": "Use a neutral historical narration style.",
        "Storytelling": "Narrate like an engaging storyteller.",
        "Dramatic": "Narrate in a dramatic and cinematic tone.",
        "First-Person": f"Narrate as if you are a historical figure who lived during a major event at {place}."
    }

    prompt = f"""
You are a professional historian.

Generate structured historical information about {place}.

{depth_map[depth]}
{audience_map[audience]}
{narration_map[narration_mode]}

Respond ONLY in valid JSON format:

{{
  "overview": "",
  "timeline": [
     {{"year": "", "event": ""}}
  ],
  "key_figures": [
     {{"name": "", "role": "", "importance": ""}}
  ],
  "interesting_facts": []
}}
"""
    return prompt