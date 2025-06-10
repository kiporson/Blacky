import time
import logging
from core import telegram_notifier

logging.basicConfig(filename='log/cpa_bomb.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run():
    links = [
        "https://cpa.example1.com",
        "https://cpa.example2.com",
        "https://cpa.example3.com"
    ]
    telegram_notifier.send_telegram_message("💣 CPA Bomb mulai dijalankan.")
    logging.info("CPA Bomb started.")

    try:
        while True:
            for link in links:
                msg = f"🔥 Mengakses CPA link: {link}"
                print(msg)
                logging.info(msg)
                telegram_notifier.send_telegram_message(msg)

                # Simulasi delay akses link CPA
                time.sleep(5)

            telegram_notifier.send_telegram_message("🎯 Semua link CPA selesai di-bomb, jeda 5 menit.")
            time.sleep(300)  # jeda 5 menit sebelum loop ulang

    except Exception as e:
        err_msg = f"⚠️ Error di CPA Bomb: {str(e)}"
        print(err_msg)
        logging.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)