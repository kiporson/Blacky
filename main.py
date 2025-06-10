import time
from core import device_spoofer, identity_generator, proxy_pool, telegram_notifier
from earn import affiliate_splitter, cpa_bomb, daily_task_grabber, push_loop, rotator_engine, shortlink_blast
from defender import behavior_simulator, captcha_skipper, proxy_rotator_guard, response_monitor
from stealth import anti_bot_flagger, fingerprint_cloak, stealth_header
from wallet_split.auto_withdraw import auto_withdraw_to_wallet
from wallet_split import mirror_wallet
import logging
import threading

logging.basicConfig(filename='log/diablo_blackhat.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def startup_banner():
    banner = "🔥 DIABLO BLACKHAT ENGINE ACTIVE 🔥"
    print(banner)
    logging.info("DIABLO system initiated.")
    telegram_notifier.send_telegram_message(banner)


def init_defense():
    telegram_notifier.send_telegram_message("🛡️ Memulai modul defense...")
    threading.Thread(target=behavior_simulator.run).start()
    threading.Thread(target=captcha_skipper.run).start()
    threading.Thread(target=proxy_rotator_guard.run).start()
    threading.Thread(target=response_monitor.run).start()


def init_stealth():
    telegram_notifier.send_telegram_message("🕵️‍♂️ Mengaktifkan stealth mode...")
    fingerprint_cloak.cloak()
    stealth_header.inject()


def init_earning():
    telegram_notifier.send_telegram_message("💰 Menyalakan semua modul penghasilan...")
    threading.Thread(target=daily_task_grabber.start).start()
    threading.Thread(target=cpa_bomb.run).start()
    threading.Thread(target=affiliate_splitter.dispatch).start()
    threading.Thread(target=push_loop.begin).start()
    threading.Thread(target=rotator_engine.spin).start()
    threading.Thread(target=shortlink_blast.fire).start()


def init_wallet_ops():
    telegram_notifier.send_telegram_message("🔄 Sinkronisasi wallet & withdraw...")
    auto_withdraw_to_wallet(amount=5)  # Sesuaikan amount jika perlu
    mirror_wallet.sync()


def main():
    startup_banner()
    telegram_notifier.send_telegram_message("🚀 DIABLO telah dinyalakan.")
    proxy_pool.initialize()
    identity_generator.generate()
    device_spoofer.spoof()
    init_defense()
    init_stealth()
    init_earning()
    init_wallet_ops()
    telegram_notifier.send_telegram_message("✅ Semua modul aktif. DIABLO berjalan normal.")
    while True:
        time.sleep(300)


if __name__ == "__main__":
    main()