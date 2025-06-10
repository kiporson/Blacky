import requests
from bs4 import BeautifulSoup

def scrape_offers(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        links = [a['href'] for a in soup.find_all('a', href=True) if "offer" in a['href'] or "cpa" in a['href']]
        return links[:10]  # Batas maksimum 10 link
    except Exception as e:
        print(f"[SCRAPER ERROR] {e}")
        return []

if __name__ == "__main__":
    sample_url = "https://www.offervault.com/"
    results = scrape_offers(sample_url)
    for link in results:
        print("CPA LINK ➤", link)
