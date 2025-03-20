from fastapi import FastAPI
from dotenv import load_dotenv

import os
import openai
import sqlite3

app = FastAPI()

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

conn = sqlite3.connect("chat_memory.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        user_id TEXT PRIMARY KEY,
        history TEXT
    )
""")


conn.commit()
