import time
import threading
import logging
from core import device_spoofer, identity_generator, proxy_pool, telegram_notifier
from earn import affiliate_splitter, cpa_bomb, daily_task_grabber, push_loop, rotator_engine, shortlink_blast
from defender import behavior_simulator, captcha_skipper, proxy_rotator_guard, response_monitor
from stealth import anti_bot_flagger, fingerprint_cloak, stealth_header
from wallet_split.auto_withdraw import auto_withdraw_to_wallet
from wallet_split import mirror_wallet
from dashboard import app  # import Flask app

logging.basicConfig(filename='log/diablo_blackhat.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_flask():
    app.run(host="0.0.0.0", port=8080)

def notify_module_start(name):
    msg = f"🚀 Modul {name} sudah aktif."
    telegram_notifier.send_telegram_message(msg)
    logging.info(msg)
    print(msg)

def startup_banner():
    banner = "🔥 DIABLO BLACKHAT ENGINE ACTIVE 🔥"
    telegram_notifier.send_telegram_message(banner)
    logging.info(banner)
    print(banner)

def init_defense():
    notify_module_start("Defense")
    threading.Thread(target=behavior_simulator.run, daemon=True).start()
    threading.Thread(target=captcha_skipper.run, daemon=True).start()
    threading.Thread(target=proxy_rotator_guard.run, daemon=True).start()
    threading.Thread(target=response_monitor.run, daemon=True).start()

def init_stealth():
    notify_module_start("Stealth")
    fingerprint_cloak.cloak()
    stealth_header.inject()

def init_earning():
    notify_module_start("Earning")
    threading.Thread(target=daily_task_grabber.start, daemon=True).start()
    threading.Thread(target=cpa_bomb.run, daemon=True).start()
    threading.Thread(target=affiliate_splitter.dispatch, daemon=True).start()
    threading.Thread(target=push_loop.begin, daemon=True).start()
    threading.Thread(target=rotator_engine.spin, daemon=True).start()
    threading.Thread(target=shortlink_blast.fire, daemon=True).start()

def init_wallet_ops():
    notify_module_start("Wallet Operations")
    threading.Thread(target=auto_withdraw_to_wallet, kwargs={'amount': 5}, daemon=True).start()
    threading.Thread(target=mirror_wallet.sync, daemon=True).start()

def main():
    threading.Thread(target=run_flask, daemon=True).start()
    startup_banner()
    proxy_pool.initialize()
    identity_generator.generate()
    device_spoofer.spoof()
    init_defense()
    init_stealth()
    init_earning()
    init_wallet_ops()
    telegram_notifier.send_telegram_message("✅ Semua modul aktif. DIABLO berjalan normal.")
    logging.info("Semua modul aktif. DIABLO berjalan normal.")
    try:
        while True:
            time.sleep(300)
    except KeyboardInterrupt:
        telegram_notifier.send_telegram_message("🛑 DIABLO dimatikan oleh user.")
        logging.info("DIABLO system terminated by user.")

if __name__ == "__main__":
    main()