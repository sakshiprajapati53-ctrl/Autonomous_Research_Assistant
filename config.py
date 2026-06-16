from dotenv import load_dotenv
from pathlib import Path
import os
# .env file ka exact path force karo
BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR / ".env"

load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE = os.getenv("ACCESS_TOKEN_EXPIRE")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print(os.getenv("DATABASE_URL"))