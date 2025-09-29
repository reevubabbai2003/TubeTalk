import streamlit as st
from RAG_pipeline import Tube_Talk # Assuming your class is in RAG_pipeline.py
import os
from dotenv import load_dotenv

# Load environment variables (API keys)
load_dotenv()

# --- Streamlit UI Configuration ---
st.set_page_config(
    page_title="TubeTalk: YouTube Video Q&A",
    page_icon="🎥",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
        border: 1px solid #ced4da;
        border-radius: 5px;
        padding: 10px;
    }
    .stTextArea>div>div>textarea {
        background-color: #ffffff;
        border: 1px solid #ced4da;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stAlert {
        border-radius: 5px;
    }
    .stMarkdown h1, h2, h3 {
        color: #333333;
    }
    .stHeader {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Dashboard Header ---
st.container()
st.image("https://img.icons8.com/color/96/000000/youtube-play.png", width=50)
st.title("TubeTalk: Ask Me Anything About YouTube Videos! 🎥")
st.markdown("Easily get answers to your questions by leveraging the power of RAG on video transcripts.")
st.markdown("---")

# --- User Inputs ---
youtube_url = st.text_input("🔗 Paste YouTube Video URL here:", key="url_input", placeholder="e.g., https://www.youtube.com/watch?v=y31hJnCBIAo")
user_question = st.text_area("❓ Your Question:", key="question_input", height=100, placeholder="e.g., What is the main topic of this video?")

# --- Process Button ---
if st.button("Get Answer! 🚀"):
    if not youtube_url:
        st.error("Please enter a YouTube video URL to proceed.")
    elif not user_question:
        st.error("Please enter a question about the video.")
    else:
        with st.spinner("Processing video and generating answer... this might take a moment!"):
            try:
                # Initialize your Tube_Talk class
                tube_talk_instance = Tube_Talk(youtube_url, user_question)

                # First, check if a transcript can be indexed
                transcript = tube_talk_instance.indexing()
                if not transcript:
                     st.warning("Could not retrieve a transcript for this video. Please check the URL or try another video with English captions.")
                else:
                    # Call the generation method and store the returned answer
                    answer = tube_talk_instance.generation()

                    # Display the answer in the dashboard
                    st.subheader("💡 Answer:")
                    st.info(answer)

            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit and Google Gemini.")