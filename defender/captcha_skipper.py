
import time

def skip_captcha():
    print("🤖 Melewati CAPTCHA... [SIMULATED]")
    return True  # Simulasi CAPTCHA terlewati

def run():
    while True:
        skip_captcha()
        time.sleep(60)
