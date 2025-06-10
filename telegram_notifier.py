import os
import requests

def notify_start():
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    message = "🔥 DIABLO TELAH AKTIF DI RAILWAY 🔥"

    if token and chat_id:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message
        }
        try:
            res = requests.post(url, data=data)
            print("📨 Telegram sent →", res.text)  # ⬅ Tambahan penting untuk log
        except Exception as e:
            print("Telegram error:", e)
    else:
        print("⚠️ TELEGRAM_TOKEN or CHAT_ID is missing in env")