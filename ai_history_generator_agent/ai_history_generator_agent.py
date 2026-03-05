# app.py
import streamlit as st
from services.local_llm_service import generate_history_local

# ====== Streamlit Page Setup ======
st.set_page_config(page_title="AI History Explorer", layout="wide")
st.title("🧭 AI History Explorer")
st.markdown("Enter a place name to explore its history in detail.")

# ====== Sidebar / Input Controls ======
st.sidebar.header("Options")

place_name = st.sidebar.text_input("Enter Place Name", "")

depth = st.sidebar.selectbox(
    "Select Depth",
    ["Quick", "Standard", "Deep Dive"]
)

audience = st.sidebar.selectbox(
    "Select Audience",
    ["Adult", "Kid", "Academic"]
)

tone = st.sidebar.selectbox(
    "Select Tone",
    ["Neutral", "Dramatic", "Storytelling"]
)

story_mode = st.sidebar.checkbox("Enable Storytelling Mode", value=False)

generate_button = st.sidebar.button("Generate History")

# ====== Main Output ======
if generate_button:
    if not place_name.strip():
        st.warning("Please enter a place name.")
    else:
        # Construct the prompt dynamically
        prompt = (
            f"Provide a {depth.lower()} history of {place_name.strip()} for a {audience.lower()} audience, tone: {tone.lower()}."
        )
        if story_mode:
            prompt += " Present it in an engaging storytelling format."
        
        # Add instruction to return structured sections
        prompt += (
            "\n\nOutput only the following sections, in this order:\n"
            "1. Overview: At least 2 sentences, no numbering, no bullet points, no metadata, no repetition of prompt.\n"
            "2. Timeline: List major events chronologically.\n"
            "3. Key Historical Figures: List notable people with short descriptions.\n"
            "4. Fun Facts: Interesting historical tidbits.\n"
            "5. Do not include the original prompt, steps, or extra conclusions.n"
        )
        
        # Call the local LLaMA model
        with st.spinner("Generating history..."):
            try:
                output_text = generate_history_local(prompt, max_tokens=800)
            except Exception as e:
                st.error(f"Error generating history: {e}")
                output_text = None

        # ====== Parse output into sections ======
        if output_text:
            sections = {"Overview": "", "Timeline": "", "Key Figures": "", "Fun Facts": ""}
            current_section = "Overview"

            for line in output_text.splitlines():
                line = line.strip()
                if line.startswith("1.") or "overview" in line.lower():
                    current_section = "Overview"
                    sections[current_section] += line + "\n"
                elif line.startswith("2.") or "timeline" in line.lower():
                    current_section = "Timeline"
                elif line.startswith("3.") or "key historical figures" in line.lower():
                    current_section = "Key Figures"
                elif line.startswith("4.") or "fun facts" in line.lower():
                    current_section = "Fun Facts"
                else:
                    sections[current_section] += line + "\n"

            # ====== Display Sections Top-Down ======
            st.subheader("Overview")
            st.text_area("Overview", sections.get("Overview", ""), height=250)

            st.subheader("Timeline of Major Events")
            st.text_area("Timeline", sections.get("Timeline", ""), height=200)

            st.subheader("Key Historical Figures")
            st.text_area("Key Figures", sections.get("Key Figures", ""), height=200)

            st.subheader("Fun Facts")
            st.text_area("Fun Facts", sections.get("Fun Facts", ""), height=150)