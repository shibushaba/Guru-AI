import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def debug_response():
    # Try WITHOUT site:
    query = "React tutorial"
    url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
    print(f"Fetching: {url}")
    
    res = requests.get(url, headers=HEADERS)
    print(f"Status: {res.status_code}")
    
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.select(".result__a")
    print(f"Found {len(results)} results via selector .result__a")

if __name__ == "__main__":
    debug_response()
