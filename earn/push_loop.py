
import time
from earn.daily_task_grabber import get_daily_tasks

def run_push_loop():
    tasks = get_daily_tasks()
    for task in tasks:
        print(f"🚀 Menjalankan tugas: {task['task']} - {task['date']}")
        time.sleep(1)
