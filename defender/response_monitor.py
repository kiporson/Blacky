
import time
def monitor_response(response):
    if response.status_code == 200:
        print("✅ Respon sukses.")
    else:
        print(f"❌ Respon gagal: {response.status_code}")

def run():
    while True:
        # Placeholder for real monitoring logic
        time.sleep(120)
