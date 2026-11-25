from src.config.settings import DATA_DIR
from src.ingestion.chunker import chunk_documents
from src.ingestion.loader import load_pdf
from src.retrieval.retriever import get_retriever
from src.vectorstore.store import build_vectorstore, load_vectorstore


def ingest(sample_name: str = "sample.pdf"):
    docs = load_pdf(DATA_DIR / sample_name)
    chunks = chunk_documents(docs)
    return build_vectorstore(chunks)


def query(question: str, k: int = 4):
    store = load_vectorstore()
    retriever = get_retriever(store, k=k)
    return retriever.invoke(question)