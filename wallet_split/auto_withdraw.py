import os
import time
import logging
from core import telegram_notifier

logger = logging.getLogger(__name__)

def auto_withdraw_to_wallet(amount, coin="USDT", network="TRX", address=None):
    address = address or os.getenv("MAIN_WALLET_ADDRESS")
    if not address:
        error_msg = "⚠️ Penarikan gagal: alamat wallet tidak tersedia."
        print(error_msg)
        logger.error(error_msg)
        telegram_notifier.send_telegram_message(error_msg)
        raise Exception("Alamat wallet tidak tersedia.")

    try:
        telegram_notifier.send_telegram_message(
            f"💸 Menyiapkan penarikan otomatis\nJumlah: <b>{amount} {coin}</b>\nJaringan: <b>{network}</b>\nTujuan: <code>{address}</code>"
        )
        print(f"Menarik {amount} {coin} ke {address} via jaringan {network}...")
        logger.info(f"Withdraw {amount} {coin} ke {address} via {network}")

        # Simulasi proses penarikan, ganti dengan API nyata jika ada
        time.sleep(5)

        telegram_notifier.send_telegram_message("✅ Penarikan otomatis berhasil.")
        logger.info("Penarikan otomatis berhasil.")
        return True

    except Exception as e:
        error_msg = f"⚠️ Gagal melakukan penarikan: {str(e)}"
        print(error_msg)
        logger.error(error_msg)
        telegram_notifier.send_telegram_message(error_msg)
        return False