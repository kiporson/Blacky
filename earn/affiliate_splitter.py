import time
import logging
from core import telegram_notifier

logger = logging.getLogger(__name__)

def process_batch(batch_number):
    try:
        msg_start = f"🔄 Memproses batch affiliate nomor {batch_number}"
        print(msg_start)
        logger.info(msg_start)
        telegram_notifier.send_telegram_message(msg_start)

        # Simulasi proses batch (ganti dengan logic sebenarnya)
        time.sleep(8)

        msg_done = f"✅ Selesai proses batch affiliate nomor {batch_number}"
        print(msg_done)
        logger.info(msg_done)
        telegram_notifier.send_telegram_message(msg_done)

    except Exception as e:
        err_msg = f"⚠️ Error saat proses batch {batch_number}: {str(e)}"
        print(err_msg)
        logger.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)

def dispatch():
    telegram_notifier.send_telegram_message("🪙 Affiliate Splitter mulai berjalan.")
    logger.info("Affiliate Splitter started.")

    try:
        while True:
            for batch_num in range(1, 4):
                process_batch(batch_num)
            telegram_notifier.send_telegram_message("🎯 Semua batch affiliate selesai, menunggu 5 menit sebelum ulang.")
            time.sleep(300)

    except Exception as e:
        err_msg = f"⚠️ Error di Affiliate Splitter: {str(e)}"
        print(err_msg)
        logger.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)