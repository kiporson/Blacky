
def get_stealth_headers():
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://google.com",
        "X-Requested-With": "XMLHttpRequest"
    }
    return headers

# Backwards compatibility wrapper so main.py can call `stealth_header.inject()`
def inject():
    """Return stealth headers for injection."""
    return get_stealth_headers()
