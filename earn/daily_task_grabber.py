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
        {"task": "Submit 5 form CPA", "date": today},
        {"task": "Cek email dan klik link", "date": today},
    ]
    return tasks

def perform_task(task):
    try:
        msg = f"📝 Memulai task: {task['task']} pada tanggal {task['date']}"
        print(msg)
        logging.info(msg)
        telegram_notifier.send_telegram_message(msg)

        # Simulasi eksekusi task (ganti dengan logika nyata)
        time.sleep(5)

        success_msg = f"✅ Task selesai: {task['task']}"
        print(success_msg)
        logging.info(success_msg)
        telegram_notifier.send_telegram_message(success_msg)

    except Exception as e:
        error_msg = f"⚠️ Error saat menjalankan task '{task['task']}': {str(e)}"
        print(error_msg)
        logging.error(error_msg)
        telegram_notifier.send_telegram_message(error_msg)

def start():
    telegram_notifier.send_telegram_message("📆 Daily Task Grabber aktif dan mulai loop kerja.")
    logging.info("Daily Task Grabber started.")
    try:
        while True:
            tasks = get_daily_tasks()
            telegram_notifier.send_telegram_message(f"🔄 Menemukan {len(tasks)} task harian untuk dikerjakan.")
            for task in tasks:
                perform_task(task)
            telegram_notifier.send_telegram_message("🎯 Semua task harian selesai, menunggu 5 menit sebelum cek ulang.")
            time.sleep(300)  # jeda 5 menit sebelum cek ulang
    except Exception as e:
        err_msg = f"⚠️ Error di daily_task_grabber: {str(e)}"
        print(err_msg)
        logging.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)