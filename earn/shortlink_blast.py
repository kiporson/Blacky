import time
import logging
from core import telegram_notifier

logging.basicConfig(filename='log/shortlink_blast.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def fire():
    telegram_notifier.send_telegram_message("🚀 Shortlink Blast mulai dijalankan.")
    shortlinks = [
        "https://shortlink.example1.com",
        "https://shortlink.example2.com",
        "https://shortlink.example3.com"
    ]
    try:
        for link in shortlinks:
            msg = f"🔗 Mengirim trafik ke shortlink: {link}"
            print(msg)
            logging.info(msg)
            telegram_notifier.send_telegram_message(msg)
            time.sleep(2)
        telegram_notifier.send_telegram_message("✅ Shortlink Blast selesai.")
    except Exception as e:
        err_msg = f"⚠️ Error di Shortlink Blast: {str(e)}"
        print(err_msg)
        logging.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)