AI History Generator Agent

Generate rich, narrated histories for any place with AI — instantly!

AI History Generator Agent is a Python-based, Streamlit-powered application that allows users to explore the history of any location in multiple narration styles. Powered by local LLMs or OpenAI, it’s designed for interactive storytelling, travel apps, and educational experiences.

Features

Multi-mode narration: Choose between formal, casual, or storytelling modes.

AI-powered history generation: Get concise, engaging histories of any city, landmark, or location.

Streamlit interface: Simple, interactive web UI for instant results.

Local LLM support: Run entirely offline with your own models.

Extendable: Add more narration modes or integrate with other AI apps in the cleverlabs-llm-suite.

Installation

Clone the repo:

git clone https://github.com/techravish/cleverlabs-llm-suite.git
cd cleverlabs-llm-suite/ai_history_generator_agent

Create a virtual environment and activate it:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Add your API key (if using OpenAI):

export OPENAI_API_KEY="your_api_key_here"
Running the App
streamlit run ai_history_generator_agent.py

Open the provided URL in your browser.

Enter the place you want a history for.

Select your preferred narration mode and generate!
