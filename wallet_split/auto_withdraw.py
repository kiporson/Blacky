import os
import requests
from core import telegram_notifier

def auto_withdraw_to_wallet(amount, coin="USDT", network="TRX", address=None):
    address = address or os.getenv("MAIN_WALLET_ADDRESS")
    if not address:
        telegram_notifier.send_telegram_message("⚠️ <b>Penarikan gagal: alamat wallet tidak tersedia.</b>")
        raise Exception("⚠️ Alamat wallet tidak tersedia.")

    # Notifikasi awal
    telegram_notifier.send_telegram_message(
        f"💸 <b>Menyiapkan penarikan otomatis</b>\n"
        f"Jumlah: <b>{amount} {coin}</b>\n"
        f"Jaringan: <b>{network}</b>\n"
        f"Tujuan: <code>{address}</code>"
    )

    # Simulasi payload API (dummy)
    payload = {
        "coin": coin,
        "network": network,
        "amount": amount,
        "address": address
    }

    # Simulasi proses penarikan
    print(f"💸 Menyiapkan penarikan otomatis {amount} {coin} ke {address} lewat jaringan {network}...")
    # Biasanya di sini request ke API exchange, contoh: requests.post("https://...", data=payload)

    # Notifikasi sukses
    telegram_notifier.send_telegram_message("✅ <b>Penarikan berhasil disimulasikan.</b>")
    return True