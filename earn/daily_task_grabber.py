import time
import logging
from core import telegram_notifier

logging.basicConfig(filename='log/daily_task_grabber.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def start():
    telegram_notifier.send_telegram_message("🚀 daily_task_grabber mulai berjalan.")
    logging.info("Daily Task Grabber started.")

    try:
        while True:
            telegram_notifier.send_telegram_message("📝 daily_task_grabber menjalankan tugas harian...")
            logging.info("Daily Task Grabber bekerja.")
            # Tambahkan logika nyata di sini
            time.sleep(300)
    except Exception as e:
        err = f"⚠️ Error di daily_task_grabber: {str(e)}"
        print(err)
        logging.error(err)
        telegram_notifier.send_telegram_message(err)