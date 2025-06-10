import os
import requests

def update():
    url = "https://raw.githubusercontent.com/PAPIPUPOR/diablo-updates/main/main.py"
    try:
        r = requests.get(url, timeout=10)
        with open("main.py", "w") as f:
            f.write(r.text)
        print("✅ Update selesai, main.py telah diperbarui.")
    except Exception as e:
        print(f"❌ Gagal update: {e}")

if __name__ == "__main__":
    update()
