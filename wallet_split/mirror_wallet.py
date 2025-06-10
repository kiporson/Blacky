import time
import logging
from core import telegram_notifier

logging.basicConfig(filename='log/mirror_wallet.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def sync():
    telegram_notifier.send_telegram_message("🪞 Mirror Wallet: sinkronisasi dimulai.")
    try:
        # Simulasi proses sinkronisasi wallet
        time.sleep(4)
        telegram_notifier.send_telegram_message("✅ Mirror Wallet: sinkronisasi selesai.")
        logging.info("Mirror Wallet: sinkronisasi berhasil.")
    except Exception as e:
        error_msg = f"⚠️ Error pada Mirror Wallet: {str(e)}"
        print(error_msg)
        logging.error(error_msg)
        telegram_notifier.send_telegram_message(error_msg)