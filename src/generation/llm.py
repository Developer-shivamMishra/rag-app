import base64
from pathlib import Path

from langchain_core.messages import HumanMessage
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI


def get_llm() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)


def generate_answer(
    llm: ChatGoogleGenerativeAI,
    docs: list[Document],
    question: str,
    pdf_path: str,
) -> str:
    context = "\n\n".join(d.page_content.strip() for d in docs if d.page_content.strip())
    pdf_b64 = base64.b64encode(Path(pdf_path).read_bytes()).decode("utf-8")

    instructions = (
        "Answer using the attached PDF as the main source."
        " If retrieved excerpts are provided, prefer matching content from the PDF."
    )
    body = f"{instructions}\n\nQuestion: {question}"
    if context:
        body = f"{instructions}\n\nRetrieved excerpts:\n{context}\n\nQuestion: {question}"

    message = HumanMessage(
        content=[
            {"type": "text", "text": body},
            {
                "type": "file",
                "source_type": "base64",
                "mime_type": "application/pdf",
                "data": pdf_b64,
            },
        ]
    )
    response = llm.invoke([message])
    return response.content