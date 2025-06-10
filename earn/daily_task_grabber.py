
import datetime

def get_daily_tasks():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    return [
        {"task": "Klik 10 iklan", "date": today},
        {"task": "Submit 5 form CPA", "date": today}
    ]
