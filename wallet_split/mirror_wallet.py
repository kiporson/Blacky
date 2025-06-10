
import os

def mirror_wallet():
    address = os.getenv("MAIN_WALLET_ADDRESS")
    print(f"🪞 Menduplikasi wallet utama: {address}")
    return {
        "wallet": address,
        "mirrored": True,
        "timestamp": "auto"
    }
