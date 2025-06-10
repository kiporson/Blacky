import datetime
import time
import logging
from core import telegram_notifier

logging.basicConfig(filename='log/daily_task_grabber.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_daily_tasks():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    tasks = [
        {"task": "Klik 10 iklan", "date": today},
        {"task": "Submit 5 form CPA", "date": today}
    ]
    return tasks

def start():
    telegram_notifier.send_telegram_message("📆 Daily Task Grabber aktif!")
    tasks = get_daily_tasks()
    for task in tasks:
        try:
            msg = f"📝 Menjalankan task: {task['task']} pada tanggal {task['date']}"
            print(msg)
            logging.info(msg)
            telegram_notifier.send_telegram_message(msg)

            # Simulasi delay task berjalan
            time.sleep(3)

            telegram_notifier.send_telegram_message(f"✅ Task selesai: {task['task']}")
        except Exception as e:
            err_msg = f"⚠️ Error saat menjalankan task: {task['task']} - {str(e)}"
            print(err_msg)
            logging.error(err_msg)
            telegram_notifier.send_telegram_message(err_msg)
    telegram_notifier.send_telegram_message("🎯 Semua task harian selesai.")