from langchain_google_genai import GoogleGenerativeAIEmbeddings

from src.config.settings import Settings


def get_embeddings():
    return GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")