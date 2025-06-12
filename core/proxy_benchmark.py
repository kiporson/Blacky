import requests
import time
import logging

logger = logging.getLogger(__name__)

def benchmark(proxy_list):
    results = []
    for proxy in proxy_list:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }
        start = time.time()
        try:
            r = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=5)
            elapsed = time.time() - start
            results.append((proxy, True, round(elapsed, 2)))
            logger.info(f"[PROXY BENCH] {proxy} OK ({elapsed:.2f}s)")
        except Exception:
            results.append((proxy, False, None))
            logger.warning(f"[PROXY BENCH] {proxy} FAIL")
    return results

if __name__ == "__main__":
    with open("core/proxies.txt") as f:
        proxy_list = f.read().splitlines()
    results = benchmark(proxy_list)
    for p, ok, t in results:
        print(f"{p} - {'OK' if ok else 'FAIL'} - {t if t else ''}")
