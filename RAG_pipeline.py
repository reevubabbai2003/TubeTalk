import os
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs

load_dotenv()

class Tube_Talk:
    def __init__(self,url,question):
        self.url = url
        self.question = question
        self.transcript = "" 

    def get_yt_id(self):
        if not isinstance(self.url, str):
            return None
        try:
            parsed_url = urlparse(self.url)

            if "youtube.com" in parsed_url.hostname:
                query_params = parse_qs(parsed_url.query)
                if 'v' in query_params:
                    return query_params['v'][0]
                path_parts = parsed_url.path.split('/')
                if len(path_parts) > 2 and path_parts[1] in ["embed", "shorts"]:
                    return path_parts[2]
            elif "youtu.be" in parsed_url.hostname:
                return parsed_url.path.split('/')[1]

        except (AttributeError, IndexError):
            return None

        return None

    def indexing(self):
        self.video_id = self.get_yt_id()
        if not self.video_id:
            print("Could not extract video ID from the URL.")
            return self.transcript 
        try:
            yt_transcript_api = YouTubeTranscriptApi()
            fetched = yt_transcript_api.fetch(self.video_id, languages=["en"])
            raw = fetched.to_raw_data()
            self.transcript = " ".join(item["text"] for item in raw)
        except TranscriptsDisabled:
            print("No captions available for this video.")
        except NoTranscriptFound:
            print("No transcript found for this video in the requested languages.")
        except Exception as e:
            print(f"Other error: {repr(e)}")
        return self.transcript

    def text_splitting(self):
        # Only proceed if transcript is not empty
        if not self.transcript:
            print("No transcript to split. Returning empty list of chunks.")
            return []
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.chunks = splitter.create_documents([self.transcript])
        return self.chunks

    def embedding_vector_store(self):
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        self.chunks = self.text_splitting()
        if not self.chunks:
            # Handle the case where no chunks are created (e.g., no transcript)
            raise ValueError("No text chunks available to create a vector store.")
        self.vector_store = FAISS.from_documents(self.chunks, self.embeddings)
        return self.vector_store

    def retriver(self):
        self.retriever = self.embedding_vector_store().as_retriever(search_type="similarity", search_kwargs={"k": 4})
        return self.retriever

    def augmentation(self):
        self.llm = ChatGoogleGenerativeAI(model='gemini-2.5-pro')
        return self.llm

    def prompt(self):
        self.prompt = PromptTemplate(
            template="""
            You are a helpful assistant.
            Answer ONLY from the provided transcript context.
            If the context is insufficient, just say you don't know.

            {context}
            Question: {question}
            """,
            input_variables = ['context', 'question']
        )
        return self.prompt

    def generation(self):
        try:
            self.retrived_docs = self.retriver().invoke(self.question)
            self.context_text = "\n\n".join(doc.page_content for doc in self.retrived_docs)
            self.final_prompt = self.prompt().invoke({"context": self.context_text, "question": self.question})
            self.answer = self.augmentation().invoke(self.final_prompt)
            return self.answer.content
        except ValueError as e:
            print(f"Error during generation: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")