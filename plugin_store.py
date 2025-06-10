import json
import os

def list_plugins():
    with open("plugin_store.json", "r") as f:
        store = json.load(f)
    for plugin in store:
        print(f"🧩 {plugin['name']} - {plugin['description']}")

if __name__ == "__main__":
    list_plugins()
