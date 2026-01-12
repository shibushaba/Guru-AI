import requests

def debug_gfg_search_content(topic):
    url = f"https://www.geeksforgeeks.org/?s={topic}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        res = requests.get(url, headers=headers, timeout=10)
        print(f"Status: {res.status_code}")
        print("Saving content to gfg_debug.html...")
        with open("gfg_debug.html", "w", encoding="utf-8") as f:
            f.write(res.text)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    debug_gfg_search_content("Selenium")
