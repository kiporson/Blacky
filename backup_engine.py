import os
import shutil
from datetime import datetime

def backup():
    src = "vault/earnings.db"
    dest_dir = "backup"
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    dest_file = os.path.join(dest_dir, f"earnings_{timestamp}.db")
    shutil.copy2(src, dest_file)
    print(f"🧪 Backup selesai ➤ {dest_file}")

if __name__ == "__main__":
    backup()
