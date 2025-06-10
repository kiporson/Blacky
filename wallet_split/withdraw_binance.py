
import requests
import time
import hmac
import hashlib
import os

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
WALLET = os.getenv("MAIN_WALLET_ADDRESS")
BASE_URL = "https://api.binance.com"

def get_timestamp():
    return int(time.time() * 1000)

def sign(params, secret):
    query = '&'.join([f"{key}={value}" for key, value in params.items()])
    return hmac.new(secret.encode('utf-8'), query.encode('utf-8'), hashlib.sha256).hexdigest()

def withdraw(amount=5):
    timestamp = get_timestamp()
    params = {
        "coin": "USDT",
        "network": "TRX",
        "address": WALLET,
        "amount": amount,
        "timestamp": timestamp
    }
    params["signature"] = sign(params, API_SECRET)
    headers = {
        "X-MBX-APIKEY": API_KEY
    }
    response = requests.post(BASE_URL + "/sapi/v1/capital/withdraw/apply", headers=headers, params=params)
    print("[🚀] BINANCE WITHDRAW RESPONSE:", response.status_code, response.text)
