import os
import importlib.util

PLUGIN_DIR = "plugins"

def load_plugins():
    if not os.path.exists(PLUGIN_DIR):
        os.makedirs(PLUGIN_DIR)
    for fname in os.listdir(PLUGIN_DIR):
        if fname.endswith(".psoul"):
            path = os.path.join(PLUGIN_DIR, fname)
            print(f"⚙️ Memuat plugin: {fname}")
            with open(path, "r") as f:
                code = f.read()
                exec(code, globals())

if __name__ == "__main__":
    load_plugins()
