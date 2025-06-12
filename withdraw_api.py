import requests
import os
from main import load_dotenv

API_ENDPOINT = "https://api.example-exchange.com/withdraw"
API_KEY = os.getenv("EXCHANGE_API_KEY")
WALLET = os.getenv("MAIN_WALLET_ADDRESS")

def withdraw(amount):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"amount": amount, "to": WALLET}
    try:
        r = requests.post(API_ENDPOINT, json=payload, headers=headers)
        print(f"📤 Withdraw response: {r.status_code} ➤ {r.text}")
    except Exception as e:
        print(f"❌ Gagal kirim withdraw: {e}")

if __name__ == "__main__":
    withdraw(25.00)
