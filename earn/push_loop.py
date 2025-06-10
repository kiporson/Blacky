import time
import logging
from core import telegram_notifier

logging.basicConfig(filename='log/push_loop.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def begin():
    telegram_notifier.send_telegram_message("🔄 Push Loop mulai berjalan.")
    try:
        for i in range(1, 5):
            msg = f"🚀 Push Loop round {i} sedang berjalan."
            print(msg)
            logging.info(msg)
            telegram_notifier.send_telegram_message(msg)
            time.sleep(2)
        telegram_notifier.send_telegram_message("✅ Push Loop selesai.")
    except Exception as e:
        err_msg = f"⚠️ Error di Push Loop: {str(e)}"
        print(err_msg)
        logging.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)