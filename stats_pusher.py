import sqlite3
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def push_stats():
    conn = sqlite3.connect("vault/earnings.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM earnings")
    total = cursor.fetchone()[0] or 0.0
    conn.close()

    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    msg = f"📈 Total earnings saat ini: ${total:.2f}"
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                  json={"chat_id": chat_id, "text": msg})

if __name__ == "__main__":
    push_stats()
