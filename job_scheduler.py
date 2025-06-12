from wallet_split.withdraw_binance import withdraw
import sqlite3

def get_current_earnings_usdt():
    """Return total earnings stored in the local database."""
    try:
        conn = sqlite3.connect("vault/earnings.db")
        cur = conn.cursor()
        cur.execute("SELECT SUM(amount) FROM earnings")
        total = cur.fetchone()[0] or 0.0
        conn.close()
        return float(total)
    except Exception:
        return 0.0

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
