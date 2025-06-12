import time
import logging
from core import telegram_notifier

logger = logging.getLogger(__name__)

def get_cpa_links():
    # Contoh daftar link CPA, bisa diupdate sesuai kebutuhan
    return [
        "https://cpa.example1.com",
        "https://cpa.example2.com",
        "https://cpa.example3.com"
    ]

def access_link(link):
    try:
        msg_start = f"🔥 Mulai akses CPA link: {link}"
        print(msg_start)
    logger.info(msg_start)
        telegram_notifier.send_telegram_message(msg_start)

        # Simulasi akses link (ganti dengan request HTTP sebenarnya jika perlu)
        time.sleep(10)

        msg_done = f"✅ Selesai akses CPA link: {link}"
        print(msg_done)
    logger.info(msg_done)
        telegram_notifier.send_telegram_message(msg_done)

    except Exception as e:
        err_msg = f"⚠️ Error saat akses CPA link '{link}': {str(e)}"
        print(err_msg)
        logger.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)

def run():
    telegram_notifier.send_telegram_message("💣 CPA Bomb mulai dijalankan.")
    logger.info("CPA Bomb started.")

    try:
        while True:
            links = get_cpa_links()
            telegram_notifier.send_telegram_message(f"🔄 Menemukan {len(links)} link CPA untuk dibombing.")
            for link in links:
                access_link(link)
            telegram_notifier.send_telegram_message("🎯 Semua link CPA selesai diakses, menunggu 5 menit sebelum siklus ulang.")
            time.sleep(300)

    except Exception as e:
        err_msg = f"⚠️ Error di CPA Bomb: {str(e)}"
        print(err_msg)
        logger.error(err_msg)
        telegram_notifier.send_telegram_message(err_msg)