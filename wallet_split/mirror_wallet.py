import time
import logging
from core import telegram_notifier

logger = logging.getLogger(__name__)

def sync():
    telegram_notifier.send_telegram_message("🪞 Mirror Wallet: sinkronisasi dimulai.")
    logger.info("Mirror Wallet sync started.")

    try:
        # Simulasi proses sinkronisasi wallet
        time.sleep(5)
        telegram_notifier.send_telegram_message("✅ Mirror Wallet: sinkronisasi selesai.")
        logger.info("Mirror Wallet sync completed.")
    except Exception as e:
        error_msg = f"⚠️ Error pada Mirror Wallet: {str(e)}"
        print(error_msg)
        logger.error(error_msg)
        telegram_notifier.send_telegram_message(error_msg)