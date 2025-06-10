import time
import logging
from core import telegram_notifier

logging.basicConfig(filename='log/shortlink_blast.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def fire():
    telegram_notifier.send_telegram_message("🚀 Shortlink Blast mulai dijalankan.")
    logging.info("Shortlink Blast started.")

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
                logging.info(msg)
                telegram_notifier.send_telegram_message(msg)
                time.sleep(2)

            telegram_notifier.send_telegram_message("✅ Shortlink Blast selesai satu siklus, menunggu 5 menit.")
            time.sleep(300)  # jeda 5 menit sebelum loop ulang

    except Exception as e:
        err_msg = f"⚠️ Error di Shortlink Blast: {str(e)}"
        print(err_msg)
        logging.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)