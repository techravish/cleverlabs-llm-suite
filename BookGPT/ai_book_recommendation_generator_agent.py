# app.py
import streamlit as st
from services.local_llm_service import generate_history_local

# ====== Streamlit Page Setup ======
st.set_page_config(page_title="AI Book Recommendation", layout="wide")
st.title("📘 AI Book Recommendation")
st.markdown("Describe a storyline or idea, and the app will recommend books that match the narrative.")

# ====== Sidebar / Input Controls ======
st.sidebar.header("Options")

story_line = st.sidebar.text_input("Describe a Story Line or Idea", "")

mood = st.sidebar.selectbox(
    "Select Mood",
    ["Cozy mystery for a relaxing weekend", "Fast-paced thriller like a movie", "Inspirational personal growth book"]
)

theme = st.sidebar.selectbox(
    "Theme",
    ["uplifting", "bittersweet", "Academic","bittersweet","Romance"]
)

tone = st.sidebar.selectbox(
    "Select Tone",
    ["Neutral", "Dramatic"]
)

story_mode = st.sidebar.checkbox("Enable Storytelling Mode", value=False)

generate_button = st.sidebar.button("Get Recommendations")

# ====== Main Output ======
if generate_button:
    if not story_line.strip():
        st.warning("Describe a storyline or idea")
    else:
        # Construct the prompt dynamically
        prompt = (
            f"Provide a Book recommendation which is a {mood.lower()} , theme is {theme.strip()}, naration tone is {tone.lower()}, where the story like is similar to: {story_line.lower()}."
        )
        if story_mode:
            prompt += " Present it is a librarian"
        
        # Add instruction to return structured sections
        prompt += (
            "\n\nOutput only the following sections, in this order:\n"
            "0. Name of the book: Provide the name of the book and Author details\n"
            "1. Overview: At least 2 sentences, no numbering, no bullet points, no metadata, no repetition of prompt.\n"
            "2. Why you'll like it: List based on mood, theme, tone selected earlier.\n"
            "3. Reading Level & Time estimation: List notable people with short descriptions.\n"
            "4. Fun Facts: Interesting tidbits from the book.\n"
            "5. Do not include the original prompt, steps, or extra conclusions.n"
        )
        
        # Call the local LLaMA model
        with st.spinner("Getting recommendation..."):
            try:
                output_text = generate_history_local(prompt, max_tokens=1600)
            except Exception as e:
                st.error(f"Error generating history: {e}")
                output_text = None

        # ====== Parse output into sections ======
        if output_text:
            sections = {"Name of the book": "", "Overview": "", "Key Figures": "", "Fun Facts": ""}
            current_section = "Name of the book"

            for line in output_text.splitlines():
                line = line.strip()
                if line.startswith("1.") or "Name of the book" in line.lower():
                    current_section = "Name of the book"
                    sections[current_section] += line + "\n"
                elif line.startswith("2.") or "Overview" in line.lower():
                    current_section = "Overview"
                elif line.startswith("3.") or "key historical figures" in line.lower():
                    current_section = "Key Figures"
                elif line.startswith("4.") or "fun facts" in line.lower():
                    current_section = "Fun Facts"
                else:
                    sections[current_section] += line + "\n"

            # ====== Display Sections Top-Down ======
            # st.subheader("Name of the book")
            st.text_area("Name of the book", sections.get("Name of the book", ""), height=250)

            # st.subheader("Overview")
            st.text_area("Overview", sections.get("Overview", ""), height=200)

            st.subheader("Key Historical Figures")
            st.text_area("Key Figures", sections.get("Key Figures", ""), height=200)

            st.subheader("Fun Facts")
            st.text_area("Fun Facts", sections.get("Fun Facts", ""), height=150)