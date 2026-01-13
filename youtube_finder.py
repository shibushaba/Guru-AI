import requests
from bs4 import BeautifulSoup
import urllib.parse


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


FAST_HINTS = ["crash course", "in 10", "quick", "basics", "beginner", "short"]
DEEP_HINTS = ["full course", "complete", "masterclass", "full tutorial", "3 hour", "2 hour"]


def score_video(title, mode):
    t = title.lower()

    score = 0

    if mode == "fast":
        for k in FAST_HINTS:
            if k in t:
                score += 3
        if "full" in t or "complete" in t:
            score -= 2

    if mode == "deep":
        for k in DEEP_HINTS:
            if k in t:
                score += 3
        if "crash" in t or "quick" in t:
            score -= 2

    # Prefer tutorials
    if "tutorial" in t or "course" in t:
        score += 1

    return score


def get_best_video(topic, mode="fast"):

    query = f"{topic} tutorial site:youtube.com"
    url = "https://duckduckgo.com/html/?q=" + urllib.parse.quote(query)

    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
    except Exception as e:
        print("Search failed:", e)
        return None

    results = []

    for a in soup.select("a.result__a"):
        title = a.get_text(strip=True)
        link = a.get("href")

        if "youtube.com" not in link:
            continue

        score = score_video(title, mode)

        results.append({
            "title": title,
            "url": link,
            "score": score
        })

    if not results:
        return None

    # Sort by best match
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    best = results[0]

    return {
        "title": best["title"],
        "url": best["url"]
    }
