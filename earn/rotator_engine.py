import time
import logging
from core import telegram_notifier

logger = logging.getLogger(__name__)

def spin():
    telegram_notifier.send_telegram_message("🌀 Rotator Engine mulai bekerja.")
    logger.info("Rotator Engine started.")

    try:
        while True:
            for i in range(1, 4):
                msg = f"🔄 Rotator round {i} aktif."
                print(msg)
                logger.info(msg)
                telegram_notifier.send_telegram_message(msg)
                time.sleep(4)  # Simulasi proses rotasi

            telegram_notifier.send_telegram_message("✅ Rotator Engine selesai satu siklus, menunggu 5 menit.")
            time.sleep(300)  # jeda 5 menit sebelum siklus ulang

    except Exception as e:
        err_msg = f"⚠️ Error di Rotator Engine: {str(e)}"
        print(err_msg)
        logger.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)