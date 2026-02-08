from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:1234@localhost:5432/wellmedica_db"
)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")