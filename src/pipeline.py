from src.ingestion.loader import load_pdf
from src.ingestion.chunker import chunk_documents
from src.embeddings.embedding import get_embedding_model
from src.retrieval.retriever import create_retriever
from src.generation.llm import get_llm, generate_answer


class RAGPipeline:
    def __init__(self):
        self.embeddings = get_embedding_model()
        self.llm = get_llm()
        self.retriever = None
        self.pdf_path = None

    def setup(self, pdf_path: str):
        self.pdf_path = pdf_path
        docs = load_pdf(pdf_path)
        chunks = chunk_documents(docs)
        self.retriever = create_retriever(chunks, self.embeddings)

    def ask(self, question: str) -> str:
        if not self.retriever or not self.pdf_path:
            raise ValueError("Run setup() before asking questions.")
        docs = self.retriever.invoke(question)
        return generate_answer(self.llm, docs, question, self.pdf_path)