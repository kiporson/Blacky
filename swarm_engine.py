import threading
from earn import cpa_bomb, push_loop, shortlink_blast

def swarm_worker(name, func):
    print(f"[{name}] Entity aktif.")
    func()

def start_swarm():
    entities = [
        ("DREAD", cpa_bomb.run),
        ("LAVI", push_loop.begin),
        ("NA'ZHAR", shortlink_blast.fire)
    ]
    for name, func in entities:
        t = threading.Thread(target=swarm_worker, args=(name, func))
        t.start()

if __name__ == "__main__":
    start_swarm()
