"""CLI entry point for basic-rag."""

from src.pipeline import ingest, query


def main() -> None:
    ingest()
    print(query("What is this document about?"))


if __name__ == "__main__":
    main()