import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def debug_response():
    # Try the failing query
    query = "React tutorial site:geeksforgeeks.org"
    url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
    print(f"Fetching: {url}")
    
    res = requests.get(url, headers=HEADERS)
    print(f"Status: {res.status_code}")
    
    soup = BeautifulSoup(res.text, "html.parser")
    print(f"Page Title: {soup.title.text if soup.title else 'No Title'}")
    
    results = soup.select(".result__a")
    print(f"Found {len(results)} results via selector .result__a")
    
    if not results:
        print("--- HTML DUMP START ---")
        print(res.text[:500])
        print("--- HTML DUMP END ---")

if __name__ == "__main__":
    debug_response()
