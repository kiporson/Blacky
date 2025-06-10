
import random
from core.proxy_pool import get_all_proxies

def rotate_proxies():
    proxies = get_all_proxies()
    selected = random.choice(proxies)
    print(f"🔐 Proxy digunakan: {selected}")
    return selected
