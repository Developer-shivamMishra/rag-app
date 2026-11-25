from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

def load_pdf(pdf_path: Path):
    pdf_path = Path("data/sample.pdf")
    loader = PyPDFLoader.from_path(file_path = pdf_path)
    docs = loader.load()
    
    if  not docs:
        raise ValueError(f"No documents found in {pdf_path}")
    
    return docs