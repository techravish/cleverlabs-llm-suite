# 🌍 AI History Generator Agent

Generate rich, narrated histories for any place with AI — instantly!

## Overview

**AI History Generator Agent** is a Python-based, Streamlit-powered application that allows users to explore the history of any location in multiple narration styles. Powered by local LLMs or OpenAI, it's designed for interactive storytelling, travel apps, and educational experiences.

![AI History Generator Agent](/docs/Banner/ai_history%20generator.png)

## ✨ Features

- 🎤 **Multi-mode narration** — Choose between formal, casual, or storytelling modes
- 🤖 **AI-powered history generation** — Get concise, engaging histories of any city, landmark, or location
- 🎨 **Streamlit interface** — Simple, interactive web UI for instant results
- 💻 **Local LLM support** — Run entirely offline with your own models
- 🔧 **Extendable** — Add more narration modes or integrate with other AI apps in the cleverlabs-llm-suite

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/techravish/cleverlabs-llm-suite.git
cd cleverlabs-llm-suite/ai_history_generator_agent
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your llama model

Get your own llama based model from huggingface based on your hardware support.
Keep the file in the model directory

## 🚀 Running the App

```bash
streamlit run ai_history_generator_agent.py
```

1. Open the provided URL in your browser
2. Enter the place you want a history for
3. Select your preferred narration mode
4. Click generate and explore!

## 📋 Usage

- **Location Input** — Type any city, landmark, or historical site
- **Narration Mode Selection** — Choose from formal, casual, or storytelling styles
- **History Generation** — Instant AI-powered historical narratives
- **Offline Support** — Works with local models for privacy and speed

## 🛠️ Built With

- **Python** — Core language (85.9%)
- **Streamlit** — Web UI framework
- **LangChain** — LLM orchestration
- **Local llama model** — Flexible AI backend & No API key needed

## 📝 License

- MIT License

## 🤝 Contributing

We welcome contributions! Feel free to open issues or submit pull requests.

## 📧 Support

For questions or issues, please open an issue on GitHub.
