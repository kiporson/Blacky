import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("⚠️ Telegram token/chat ID belum diset.")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload)
        print("📨 Telegram sent →", response.text)
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Gagal kirim Telegram: {e}")
        return False

# 🔥 Fungsi yang dipanggil dari dashboard.py
def notify_start():
    send_telegram_message("🔥 DIABLO TELAH AKTIF DI RAILWAY 🔥")