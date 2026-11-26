from pypdf import PdfReader
from langchain_core.documents import Document

def load_pdf(file_path: str) -> list[Document]:
    reader = PdfReader(file_path)
    return [
        Document(
            page_content=page.extract_text() or "",
            metadata={"source": file_path, "page": i},
        )
        for i, page in enumerate(reader.pages)
    ]