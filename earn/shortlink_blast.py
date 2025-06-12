import time
import logging
from core import telegram_notifier

logger = logging.getLogger(__name__)

def fire():
    telegram_notifier.send_telegram_message("🚀 Shortlink Blast mulai dijalankan.")
    logger.info("Shortlink Blast started.")

    shortlinks = [
        "https://shortlink.example1.com",
        "https://shortlink.example2.com",
        "https://shortlink.example3.com"
    ]

    try:
        while True:
            for link in shortlinks:
                msg = f"🔗 Mengirim trafik ke shortlink: {link}"
                print(msg)
                logger.info(msg)
                telegram_notifier.send_telegram_message(msg)
                time.sleep(3)  # Simulasi delay trafik

            telegram_notifier.send_telegram_message("✅ Shortlink Blast selesai satu siklus, menunggu 5 menit.")
            time.sleep(300)  # jeda 5 menit sebelum siklus ulang

    except Exception as e:
        err_msg = f"⚠️ Error di Shortlink Blast: {str(e)}"
        print(err_msg)
        logger.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)