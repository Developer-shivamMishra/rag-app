from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def load_pdf(path: Path):
    return PyPDFLoader(str(path)).load()