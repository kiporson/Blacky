import requests
from bs4 import BeautifulSoup

def collect_leads(source_url="https://example.com"):
    try:
        r = requests.get(source_url, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        leads = [a['href'] for a in soup.find_all('a', href=True) if "signup" in a['href'] or "join" in a['href']]
        print(f"📥 {len(leads)} lead ditemukan:")
        for l in leads[:10]:
            print("➡️", l)
        return leads
    except Exception as e:
        print(f"❌ Gagal mengambil lead: {e}")
        return []

if __name__ == "__main__":
    collect_leads()
