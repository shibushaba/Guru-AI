import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def debug_response():
    # Try WITHOUT site:
    query = "React tutorial"
    url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
    print(f"Fetching: {url}")
    
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        print(f"Status: {res.status_code}")
        
        soup = BeautifulSoup(res.text, "html.parser")
        results = soup.select(".result__a")
        print(f"Found {len(results)} results")
        if len(results) > 0:
            print(f"First: {results[0].text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_response()
