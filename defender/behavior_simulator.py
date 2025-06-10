
import time
import random

def simulate_human_behavior():
    print("🧠 Simulasi perilaku manusia...")
    time.sleep(random.uniform(0.5, 2.0))
    actions = ['scroll', 'click', 'pause', 'hover']
    for _ in range(random.randint(3, 6)):
        action = random.choice(actions)
        print(f"⚙️ Aksi: {action}")
        time.sleep(random.uniform(0.3, 1.2))
