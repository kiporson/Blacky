import time
import logging
from core import telegram_notifier

logging.basicConfig(filename='log/affiliate_splitter.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def dispatch():
    telegram_notifier.send_telegram_message("🪙 Affiliate Splitter mulai berjalan.")
    try:
        # Contoh proses split affiliate
        for i in range(1, 4):
            msg = f"🔄 Memproses batch affiliate ke-{i}"
            print(msg)
            logging.info(msg)
            telegram_notifier.send_telegram_message(msg)
            # Simulasi delay pemrosesan batch
            time.sleep(3)
        telegram_notifier.send_telegram_message("✅ Affiliate Splitter selesai memproses semua batch.")
    except Exception as e:
        err_msg = f"⚠️ Error di Affiliate Splitter: {str(e)}"
        print(err_msg)
        logging.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)