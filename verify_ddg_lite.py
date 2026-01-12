import requests
from bs4 import BeautifulSoup

def verify_lite():
    url = "https://lite.duckduckgo.com/lite/"
    data = {"q": "Selenium documentation tutorial"}
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    try:
        res = requests.post(url, data=data, headers=headers, timeout=20)
        print(f"Status: {res.status_code}")
        print("-" * 20)
        print(res.text[:2000]) # First 2000 chars
        print("-" * 20)
        
        soup = BeautifulSoup(res.text, "html.parser")
        links = soup.select(".result-link")
        print(f"Found {len(links)} result-link class links.")
        
        all_links = soup.find_all("a")
        print(f"Found {len(all_links)} total links.")
        for i, a in enumerate(all_links):
            if i < 10:
                print(f"All Link {i}: {a.get('href')}")
                
    except Exception as e:
        print(e)

if __name__ == "__main__":
    verify_lite()
