import os
import subprocess

def start_main():
    print("🔁 Menjalankan DIABLO BLACKHAT ENGINE...")
    os.system("python3 main.py")

def run_test():
    print("🧪 Menjalankan semua pengujian...")
    os.system("pytest tests/")

if __name__ == "__main__":
    start_main()
