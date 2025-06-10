from wallet_split.withdraw_binance import withdraw

def check_and_withdraw_if_earnings_exist():
    earnings = get_current_earnings_usdt()  # Fungsi internal
    if earnings >= 0.01:
        print(f"[💸] Detected earnings: ${earnings} — initiating withdraw.")
        withdraw(amount=earnings)

from apscheduler.schedulers.background import BackgroundScheduler
from earn import cpa_bomb, push_loop, shortlink_blast
import time

def schedule_jobs():
    scheduler = BackgroundScheduler()
    scheduler.add_job(cpa_bomb.run, 'interval', minutes=30)
    scheduler.add_job(push_loop.begin, 'interval', minutes=45)
    scheduler.add_job(shortlink_blast.fire, 'interval', minutes=60)
    scheduler.start()
    print("🕒 Job Scheduler aktif.")
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        scheduler.shutdown()

if __name__ == "__main__":
    schedule_jobs()
