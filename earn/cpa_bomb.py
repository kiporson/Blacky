
import time

def bomb_cpa_links(links, interval=2):
    for link in links:
        print(f"🔥 Mengakses: {link}")
        time.sleep(interval)
