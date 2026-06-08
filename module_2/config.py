import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

API_KEY = os.environ.get("google_api_key")
MODEL = "gemini-2.5-flash-lite"
