import time
import logging
from core import telegram_notifier

logging.basicConfig(filename='log/rotator_engine.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def spin():
    telegram_notifier.send_telegram_message("🌀 Rotator Engine mulai bekerja.")
    logging.info("Rotator Engine started.")

    try:
        while True:
            for i in range(1, 4):
                msg = f"🔄 Rotator round {i} aktif."
                print(msg)
                logging.info(msg)
                telegram_notifier.send_telegram_message(msg)
                time.sleep(4)  # Simulasi proses rotasi

            telegram_notifier.send_telegram_message("✅ Rotator Engine selesai satu siklus, menunggu 5 menit.")
            time.sleep(300)  # jeda 5 menit sebelum siklus ulang

    except Exception as e:
        err_msg = f"⚠️ Error di Rotator Engine: {str(e)}"
        print(err_msg)
        logging.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)