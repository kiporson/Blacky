import requests

def is_valid_offer(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200 and any(k in r.text.lower() for k in ["offer", "signup", "earn"]):
            return True
    except:
        return False
    return False

if __name__ == "__main__":
    print(is_valid_offer("https://example.com"))
