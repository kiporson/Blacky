import time
from core import telegram_notifier

# Daftar dummy CPA links untuk simulasi
CPA_LINKS = [
    "https://cpa-network.com/offer1",
    "https://cpa-network.com/offer2",
    "https://cpa-network.com/offer3"
]

def run():
    telegram_notifier.send_telegram_message("💣 <b>Memulai serangan CPA Bomb...</b>")
    for link in CPA_LINKS:
        print(f"🔥 Mengakses: {link}")
        telegram_notifier.send_telegram_message(f"➡️ <b>Mengakses:</b> {link}")
        time.sleep(2)
    telegram_notifier.send_telegram_message("✅ <b>CPA Bomb selesai dijalankan.</b>")