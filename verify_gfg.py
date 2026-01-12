import requests
from bs4 import BeautifulSoup

def test_gfg_search(topic):
    url = f"https://www.geeksforgeeks.org/search?q={topic}"
    # or just ?q=
    # Actually GFG search is often GCse (Google Custom Search).
    # Let's try the native search if it exists?
    # Old search: https://www.geeksforgeeks.org/?s=selenium
    
    url = f"https://www.geeksforgeeks.org/?s={topic}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        res = requests.get(url, headers=headers)
        print(f"Status: {res.status_code}")
        print("-" * 20)
        print(res.text[:4000]) # First 4000 chars
        print("-" * 20)
        soup = BeautifulSoup(res.text, "html.parser")
        # Look for result titles
        # Usually 'a' inside 'header.entry-header' or similar
        # Or 'div.searching_result' ?
        
        # Let's inspect potential links
        links = soup.select("a")
        found = 0
        print(f"Total links found: {len(links)}")
        for i, a in enumerate(links):
            href = a.get("href", "")
            if i < 20: print(f"Link {i}: {href}")
            
            if "geeksforgeeks" in href or href.startswith("/"):
                 if topic.lower() in href.lower() or "tutorial" in href.lower():
                    print(f"Possible: {href}")
                    found += 1

        
        if found == 0:
            print("No links found via direct scraping.")
            
    except Exception as e:
        print(e)

if __name__ == "__main__":
    test_gfg_search("selenium")
