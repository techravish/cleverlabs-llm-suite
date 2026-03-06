# app.py

import streamlit as st
import json
import re
from services.local_llm_service import generate_history_local

# ====== Streamlit Page Setup ======
st.set_page_config(page_title="AI Book Recommendation", layout="wide")
# Centered title
st.markdown("<h1 style='text-align: center;'>📘 AI Book Recommendation</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Describe a storyline or idea, and the AI will recommend a book that matches the narrative.</h3>", unsafe_allow_html=True)

# ====== Sidebar ======
st.sidebar.header("Recommendation Options")

story_line = st.sidebar.text_input("Describe a Story Line or Idea")

mood = st.sidebar.selectbox(
    "Select Mood",
    [
        "Cozy mystery for a relaxing weekend",
        "Fast-paced thriller like a movie",
        "Inspirational personal growth book",
    ],
)

theme = st.sidebar.selectbox(
    "Theme",
    ["Uplifting", "Bittersweet", "Academic", "Romance"],
)

tone = st.sidebar.selectbox(
    "Select Tone",
    ["Neutral", "Dramatic"],
)

story_mode = st.sidebar.checkbox("Enable Storytelling Mode", value=False)

generate_button = st.sidebar.button("Get Recommendation")

# ====== Generate Recommendation ======
if generate_button:

    if not story_line.strip():
        st.warning("Please describe a storyline or idea.")
        st.stop()

    # ====== Prompt Construction ======
    prompt = f"""
You are an expert librarian recommending books.

Based on the preferences below, recommend EXACTLY ONE book.

Mood: {mood.lower()}
Theme: {theme.lower()}
Narrative Tone: {tone.lower()}
Similar Storyline: {story_line.lower()}

Return ONLY valid JSON using this exact structure:

{{
  "book_name": "string",
  "author": "string",
  "overview": "2-3 sentence description of the book",
  "why_youll_like_it": [
    "reason 1",
    "reason 2",
    "reason 3"
  ],
  "reading_level": "Select a reading level Beginner | Intermediate | Advanced",
  "estimated_reading_time": "Estimate approximate time to finish the book",
  "fun_facts": [
    "fact 1",
    "fact 2"
  ]
}}

Rules:
- Recommend exactly ONE book.
- Return ONLY valid JSON.
- No markdown.
- No explanations.
- No trailing commas.
- Do not include text before or after JSON.
"""

    # ====== Call LLM and Parse JSON ======
    with st.spinner("Getting recommendation..."):

        try:
            response = generate_history_local(prompt, max_tokens=2000)

            # Clean LLM formatting
            response = response.replace("```json", "").replace("```", "").strip()

            # Remove trailing commas
            response = re.sub(r",\s*([\]}])", r"\1", response)

            # Extract first JSON object
            json_match = re.search(r"\{.*?\}", response, re.DOTALL)

            if not json_match:
                raise ValueError("No valid JSON found in model response")

            json_text = json_match.group()

            data = json.loads(json_text)

        except Exception as e:
            st.error(f"Error generating recommendation: {e}")
            st.text(response)
            st.stop()

    # ====== Display Output ======
    if data:
        st.header(data.get("book_name", "Unknown Book"))
        st.subheader(f"by {data.get('author', 'Unknown Author')}")

        st.write(data.get("overview", ""))

        st.subheader("Why you'll like it")
        for reason in data.get("why_youll_like_it", []):
            st.write(f"• {reason}")

        st.subheader("Reading Level")
        st.write(data.get("reading_level", ""))

        st.subheader("Estimated Reading Time")
        st.write(data.get("estimated_reading_time", ""))

        st.subheader("Fun Facts")
        for fact in data.get("fun_facts", []):
            st.write(f"• {fact}")