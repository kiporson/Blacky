import time
import logging
from core import telegram_notifier

logger = logging.getLogger(__name__)

def begin():
    telegram_notifier.send_telegram_message("🔄 Push Loop mulai berjalan.")
    logger.info("Push Loop started.")

    try:
        while True:
            for i in range(1, 6):
                msg = f"🚀 Push Loop round {i} sedang berjalan."
                print(msg)
                logger.info(msg)
                telegram_notifier.send_telegram_message(msg)
                time.sleep(3)  # Simulasi kerja tiap round

            telegram_notifier.send_telegram_message("✅ Push Loop selesai satu siklus, menunggu 5 menit.")
            time.sleep(300)  # jeda 5 menit sebelum loop ulang

    except Exception as e:
        err_msg = f"⚠️ Error di Push Loop: {str(e)}"
        print(err_msg)
        logger.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)