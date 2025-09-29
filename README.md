# TubeTalk

TubeTalk is a lightweight Streamlit web app that lets you **have a conversation with any YouTube video**. Provide a YouTube URL and a question — TubeTalk fetches the transcript, retrieves the most relevant transcript chunks using FAISS, and uses Google's Gemini model to generate a context-aware answer constrained to the transcript.

---

## ✨ Features

* **Automatic YouTube transcript extraction** (English transcripts)
* **RAG-powered Q&A**: LangChain text splitting + FAISS vector store for fast retrieval
* **Gemini (Google) generation**: Model answers using retrieved transcript context
* **Streamlit UI**: Minimal, modern dashboard for quick interaction
* **Safe-by-design**: Model is instructed to answer only from the transcript to reduce hallucinations

---


## ✅ Prerequisites

* Python 3.9+
* `pip` (or `pip3`) or `conda` for managing packages
* A Google API key with access to Gemini models (obtain from Google AI Studio / Google Cloud Console)

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/your-username/TubeTalk.git
cd TubeTalk

# 2. Create & activate virtual environment
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env
# In the project root create a file named .env with the following:
# GOOGLE_API_KEY="YOUR_API_KEY_HERE"

# 5. Run
streamlit run app.py

## ⚙️ Environment variables

Create a `.env` file in the project root with the following key(s):

```env
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```


