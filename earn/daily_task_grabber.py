import datetime
import time
from core import telegram_notifier

def get_daily_tasks():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    return [
        {"task": "Klik 10 iklan", "date": today},
        {"task": "Submit 5 form CPA", "date": today}
    ]

def start():
    tasks = get_daily_tasks()
    for task in tasks:
        # Simulasi pengerjaan tugas
        print(f"🔧 Menjalankan: {task['task']}")
        telegram_notifier.send_telegram_message(f"⚙️ <b>Menjalankan Tugas:</b> {task['task']}")
        time.sleep(3)  # Delay simulasi
    telegram_notifier.send_telegram_message("✅ <b>Semua tugas harian selesai dijalankan.</b>")