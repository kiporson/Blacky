import requests
import time
import random

ROTATOR_LINKS = [
    "https://shortlink1.io/abc",
    "https://cointiply.com/ads",
    "https://paidclick.net/reward"
]

def send_clicks():
    print("📈 Mengirim trafik otomatis ke rotator...")
    for _ in range(10):
        url = random.choice(ROTATOR_LINKS)
        try:
            r = requests.get(url, timeout=5)
            print(f"➡️ Klik ke {url} ➤ Status: {r.status_code}")
        except Exception as e:
            print(f"❌ Gagal klik: {e}")
        time.sleep(random.uniform(1.2, 3.5))

if __name__ == "__main__":
    send_clicks()
