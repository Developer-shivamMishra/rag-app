from dotenv import load_dotenv

load_dotenv()

from src.pipeline import RAGPipeline

def main():
    rag = RAGPipeline()
    print("Loading DBMS_Notes (2).pdf...")
    rag.setup("DSA.pdf")

    while True:
        question = input("Ask: ")
        if question.strip().lower() in ("exit", "quit"):
            break
        print(f"\nAnswer:\n{rag.ask(question)}\n")

if __name__ == "__main__":
    main()