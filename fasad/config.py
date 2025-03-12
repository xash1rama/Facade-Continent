from dotenv import load_dotenv
import os

load_dotenv()


DB_URL = os.getenv("DB_URL")
API_KEY_BOT = os.getenv("API_KEY_BOT")
ID_CHAT = os.getenv("ID_CHAT")
PASSWORD = os.getenv("PASSWORD")
LOGIN = os.getenv("LOGIN")

