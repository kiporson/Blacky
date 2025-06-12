import time
import logging
from core import telegram_notifier

logger = logging.getLogger(__name__)

def start():
    telegram_notifier.send_telegram_message("🚀 daily_task_grabber mulai berjalan.")
    logger.info("Daily Task Grabber started.")

    try:
        while True:
            telegram_notifier.send_telegram_message("📝 daily_task_grabber menjalankan tugas harian...")
            logger.info("Daily Task Grabber bekerja.")
            # Tambahkan logika nyata di sini
            time.sleep(300)
    except Exception as e:
        err = f"⚠️ Error di daily_task_grabber: {str(e)}"
        print(err)
        logger.error(err)
        telegram_notifier.send_telegram_message(err)