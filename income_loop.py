import time
from earn import cpa_bomb, push_loop, shortlink_blast

def run_loop():
    print("💸 Memulai loop earning otomatis...")
    while True:
        cpa_bomb.run()
        push_loop.begin()
        shortlink_blast.fire()
        time.sleep(3600)  # jeda 1 jam

if __name__ == "__main__":
    run_loop()
