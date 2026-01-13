import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def find_best_reading(topic):

    query = f"{topic} explained for beginners"
    url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"

    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")

    results = []

    for a in soup.select(".result__a"):
        results.append({
            "title": a.text,
            "url": a.get("href")
        })

    # Prefer learning sites
    for r in results:
        if any(site in r["url"] for site in [
            "geeksforgeeks",
            "wikipedia",
            "investopedia",
            "khanacademy",
            "byjus",
            "tutorialspoint"
        ]):
            return r

    return results[0] if results else None
