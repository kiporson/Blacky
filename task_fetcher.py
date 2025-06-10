import requests
import json

def fetch_remote_tasks(url="https://raw.githubusercontent.com/youruser/diablo-tasks/main/task.json"):
    try:
        r = requests.get(url, timeout=10)
        tasks = r.json()
        with open("task.json", "w") as f:
            json.dump(tasks, f, indent=2)
        print("✅ Task remote berhasil diunduh.")
    except Exception as e:
        print(f"❌ Gagal fetch task: {e}")

if __name__ == "__main__":
    fetch_remote_tasks()
