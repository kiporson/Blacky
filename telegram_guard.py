import os
import requests
from main import load_dotenv

token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

def notify(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json={
            "chat_id": chat_id, "text": msg
        })
    except Exception as e:
        print("❌ Gagal kirim pesan:", e)

if __name__ == "__main__":
    notify("🛡️ DIABLO Guard aktif. Sistem dilindungi.")
