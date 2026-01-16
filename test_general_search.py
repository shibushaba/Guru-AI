from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup

def test_ddgs_lib():
    print("Testing DDGS Lib...")
    try:
        results = DDGS().text("Rust programming tutorial", max_results=3)
        print(f"DDGS Res: {len(results) if results else 0}")
        if results:
            print(results[0])
    except Exception as e:
        print(f"DDGS Error: {e}")

def test_google_scrape():
    # Very basic Google scrape attempt (unreliable but trying)
    print("Testing Google Scrape...")
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        res = requests.get("https://www.google.com/search?q=Rust+programming+tutorial", headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        # Google generic selector for results
        # Look for h3 inside a tag
        found = False
        for g in soup.find_all('div', class_='g'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3')
                if title and link.startswith("http"):
                    print(f"Google Res: {title.text} - {link}")
                    found = True
                    break
        if not found:
            print("Google: No results parsed")
            
    except Exception as e:
        print(f"Google Error: {e}")

if __name__ == "__main__":
    test_ddgs_lib()
    print("-" * 20)
    test_google_scrape()
