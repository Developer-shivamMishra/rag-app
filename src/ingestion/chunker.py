from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config.settings import Settings


def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=Settings.chunk_size,
        chunk_overlap=Settings.chunk_overlap,
    )
    return splitter.split_documents(documents)