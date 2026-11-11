
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    origins = os.getenv("ORIGINS", "http://localhost:5173")
    secret_key = os.getenv("SECRET_KEY")
    db_url = os.getenv("DB_URL")

setting = Settings()

    