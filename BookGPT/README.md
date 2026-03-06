# 📘 BookGPT – AI-Powered Book Recommendation App

![BookGPT Working](docs/Banner/Screenshot 2026-03-06 at 10.31.42 PM.png)

**BookGPT** is a Streamlit-based AI app that recommends books based on a user-provided storyline, mood, theme, and narrative tone. It leverages a local LLM (LLaMA) to generate structured book recommendations, including overviews, reasons to read, reading level, estimated reading time, and fun facts.

---

## 🚀 Features

* **Dynamic Book Recommendation:** Generate book suggestions from any storyline or idea.
* **Mood, Theme & Tone Selection:** Tailor recommendations based on your preferred mood, theme, and narrative tone.
* **Storytelling Mode:** Optionally generate a short story snippet to enrich recommendations.
* **Structured Output:** JSON-based response includes:

  * Book Name & Author
  * Overview
  * Why You’ll Like It
  * Reading Level & Estimated Time
  * Fun Facts
* **Robust Local LLM Integration:** Works with local LLaMA models or fallback mock responses.
* **Clean, Interactive UI:** Built with Streamlit, fully responsive and user-friendly.

---

## 📁 Project Structure

```
BookGPT/
│
├── app.py                     # Main Streamlit application
├── services/
│   └── local_llm_service.py   # LLM wrapper (local or mock)
├── models/                    # Place LLaMA GGUF model here
│   └── llama-3.2-1b-instruct-q8_0.gguf
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 💻 Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/techravish/cleverlabs-llm-suite.git
cd cleverlabs-llm-suite/BookGPT
```

### 2. Create a virtual environment

```
python -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add LLaMA model (optional but recommended)

Place your LLaMA GGUF model in the models folder:

```
models/llama-3.2-1b-instruct-q8_0.gguf
```

If the model is not available, the app will use a **mock response for testing**.

### 5. Run the application

```
streamlit run app.py
```

---

## 🎛 How to Use

1. Enter a **short storyline or idea** in the sidebar.
2. Select the **Mood**, **Theme**, and **Narrative Tone**.
3. Optionally enable **Storytelling Mode**.
4. Click **Get Recommendation**.

The app will generate:

* 📖 Book Name & Author
* 🧾 Overview
* ❤️ Why You’ll Like It
* 📚 Reading Level
* ⏱ Estimated Reading Time
* 🎉 Fun Facts

---

## 🛠 Tech Stack

* **Python 3**
* **Streamlit** – UI framework
* **LLaMA / llama-cpp-python** – Local LLM inference
* **JSON & Regex** – Structured response parsing

---

## 💡 Notes

* Designed to run **locally with an LLM model**.
* Can operate in **mock mode** for quick testing without downloading large models.
* Works well with **GGUF models compatible with llama-cpp**.

---

## 🔮 Future Improvements

* Multiple book recommendations
* Book cover images using OpenLibrary API
* Goodreads ratings integration
* “Find Similar Books” feature
* Personalized reading history

---

## 📄 License

MIT License
