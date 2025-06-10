
def detect_bot_footprint(headers):
    suspicious_keywords = ['bot', 'crawl', 'spider', 'scrapy', 'python-requests']
    for key, value in headers.items():
        for suspect in suspicious_keywords:
            if suspect in value.lower():
                print(f"🚫 Bot terdeteksi: {value}")
                return True
    print("✅ Tidak ada jejak bot.")
    return False
