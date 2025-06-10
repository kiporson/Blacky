
def monitor_response(response):
    if response.status_code == 200:
        print("✅ Respon sukses.")
    else:
        print(f"❌ Respon gagal: {response.status_code}")
