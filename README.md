# basic-rag

Minimal RAG layout: ingest PDFs, embed, store in Chroma, retrieve chunks.

## Setup

```bash
cd basic-rag
pip install -r requirements.txt
cp .env.example .env
```

Set `GEMINI_API_KEY` in `.env`, then run:

```bash
python app.py
```