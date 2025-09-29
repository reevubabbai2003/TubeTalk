# TubeTalk: YouTube Video Q&A 🎥

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io)
[![LLM](https://img.shields.io/badge/LLM-Google%20Gemini-purple.svg)](https://ai.google.dev/)

TubeTalk is a web application that allows you to have a conversation with any YouTube video. Simply provide a video URL and ask a question, and the app will use a Retrieval-Augmented Generation (RAG) pipeline to analyze the video's transcript and provide a context-aware answer.

---

## ✨ Features

-   **YouTube Transcript Extraction:** Automatically fetches the English transcript of any YouTube video.
-   **Modern Web Interface:** A clean and user-friendly dashboard built with Streamlit.
-   **RAG-Powered Q&A:** Leverages the power of Google Gemini and FAISS vector search to find the most relevant information within the video to answer your questions.
-   **Context-Aware Answers:** The model is instructed to answer **only** from the provided transcript, preventing hallucinations and ensuring factual responses based on the video's content.

---

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

-   Python 3.9 or higher
-   `pip` package manager

### 2. Clone the Repository

```bash
git clone [https://github.com/your-username/TubeTalk.git](https://github.com/reevubabbai2003/TubeTalk.git)
cd TubeTalk

### 3. Create a Virtual Environment

### 4. install Dependencies
pip install -r requirements.txt

### 5. Set Up Environment Variables
GOOGLE_API_KEY="YOUR_API_KEY_HERE"

### Usage
streamlit run app.py
