from langchain_google_genai import GoogleGenerativeAIEmbeddings


def get_embeddings():
    return GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")


get_embedding_model = get_embeddings