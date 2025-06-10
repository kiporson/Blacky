import json
import time
import importlib

def run_task(task):
    module = importlib.import_module(task["module"])
    func = getattr(module, task["function"])
    print(f"▶️ Menjalankan: {task['module']}.{task['function']}()")
    func()

def main():
    with open("task.json", "r") as f:
        tasks = json.load(f)
    for task in tasks:
        run_task(task)
        time.sleep(task.get("delay", 5))

if __name__ == "__main__":
    main()
