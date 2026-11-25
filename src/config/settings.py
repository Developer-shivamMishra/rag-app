from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv()

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
VECTORSTORE_DIR = ROOT / "vectorstore"


class Settings:
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    chunk_size: int = 500
    chunk_overlap: int = 50