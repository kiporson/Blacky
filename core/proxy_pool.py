import random
import os
import requests

def fetch_external_proxies():
    url = os.getenv("PROXY_API_SOURCE")
    if not url:
        return []
    try:
        res = requests.get(url, timeout=5)
        return res.text.strip().splitlines()
    except Exception as e:
        print("❌ Gagal ambil proxy dari API:", e)
        return []

PROXIES = fetch_external_proxies() or [
    "http://123.45.67.89:8080",
    "http://98.76.54.32:3128",
    "http://111.222.333.444:8000",
    "http://185.45.12.99:1080",
    "http://200.100.50.25:9999"
]

def get_random_proxy():
    return random.choice(PROXIES)

def get_all_proxies():
    return PROXIES