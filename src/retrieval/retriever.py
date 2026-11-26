from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
def create_retriever(chunks: list[Document], embeddings):
    vector_store = InMemoryVectorStore(embeddings)
    vector_store.add_documents(documents=chunks)
    return vector_store.as_retriever(search_kwargs={"k": 4})