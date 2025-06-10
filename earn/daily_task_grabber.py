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
        msg_start = f"📝 Memulai task: {task['task']} pada tanggal {task['date']}"
        print(msg_start)
        logging.info(msg_start)
        telegram_notifier.send_telegram_message(msg_start)

        # Simulasi waktu eksekusi task
        time.sleep(10)

        msg_done = f"✅ Task selesai: {task['task']}"
        print(msg_done)
        logging.info(msg_done)
        telegram_notifier.send_telegram_message(msg_done)

    except Exception as e:
        err_msg = f"⚠️ Error saat menjalankan task '{task['task']}': {str(e)}"
        print(err_msg)
        logging.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)

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