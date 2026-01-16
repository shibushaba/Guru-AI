import requests
from bs4 import BeautifulSoup
import random

UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
    # The simple one that worked before
    "Mozilla/5.0"
]

def test_ua():
    query = "React tutorial"
    url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
    
    for ua in UAS:
        print(f"Testing UA: {ua[:50]}...")
        try:
            headers = {"User-Agent": ua}
            res = requests.get(url, headers=headers, timeout=5)
            print(f"Status: {res.status_code}")
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                results = soup.select(".result__a")
                print(f"Found {len(results)} results")
                if len(results) > 0:
                    print("SUCCESS!")
                    return
            else:
                print("Failed (HTML/Status)")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_ua()
