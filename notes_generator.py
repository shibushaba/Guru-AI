import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, unquote


def clean_url(url):
    # Fix URLs starting with //
    if url.startswith("//"):
        url = "https:" + url

    # Handle DuckDuckGo redirect links
    if "duckduckgo.com/l/?" in url:
        parsed = urlparse(url)
        qs = parse_qs(parsed.query)
        if "uddg" in qs:
            url = unquote(qs["uddg"][0])

    return url


def generate_notes(url):
    try:
        url = clean_url(url)

        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        notes = []

        # Get first few meaningful paragraphs
        for p in soup.find_all("p"):
            text = p.get_text().strip()
            if len(text) > 60:
                notes.append(text)
            if len(notes) >= 6:
                break

        # Shorten notes
        short_notes = []
        for n in notes:
            if len(n) > 200:
                n = n[:200] + "..."
            short_notes.append(n)

        return short_notes

    except Exception as e:
        print(f"Notes error: {e}")
        return [
            "⚠️ Could not automatically extract detailed notes from this page.",
            "Please open the link above to read the full tutorial.",
            "Focus on understanding the core concepts and syntax."
        ]
    
    if not notes:
        return [
            "⚠️ Automated note extraction returned no content.",
             "Please click the link above to read the article directly.",
             "Summarize the key points yourself as you read."
        ]
    
    return short_notes
