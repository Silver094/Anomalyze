import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def generate_embeddings(log_lines):
    response = genai.embed_content(
        model='gemini-embedding-001',
        content=log_lines
    )
    return response['embedding']
