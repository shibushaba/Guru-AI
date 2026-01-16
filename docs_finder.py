import requests
from bs4 import BeautifulSoup
import urllib.parse
import random

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

PREFERRED_SITES = {
    "tech": [
        "geeksforgeeks.org",
        "w3schools.com",
        "developer.mozilla.org",
        "tutorialspoint.com",
        "freecodecamp.org",
        "javatpoint.com"
    ],
    "science": [
        "wikipedia.org",
        "britannica.com",
        "nationalgeographic.com",
        "livescience.com",
        "nasa.gov",
        "space.com"
    ],
    "business": [
        "investopedia.com",
        "forbes.com",
        "bloomberg.com",
        "hbr.org",
        "marketwatch.com"
    ],
    "general": [
        "wikipedia.org",
        "britannica.com",
        "wikihow.com"
    ]
}

def perform_search(query):
    """
    Helper to perform the actual DDG HTML search scrape.
    """
    url = f"https://duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        res.raise_for_status() # Check for HTTP errors
        soup = BeautifulSoup(res.text, "html.parser")

        results = []
        for a in soup.select(".result__a"):
            title = a.get_text(strip=True)
            link = a.get("href")
            
            # Simple validation
            if link and title:
                results.append({"title": title, "url": link})
        
        return results
    except Exception as e:
        print(f"Search error for '{query}': {e}")
        return []

def find_best_reading(topic, domain="general"):
    if not domain or domain not in PREFERRED_SITES:
        domain = "general"

    # ----------------------------------------
    # STRATEGY 1: Targeted Domain Search
    # ----------------------------------------
    sites = PREFERRED_SITES.get(domain, PREFERRED_SITES["general"])
    
    # Construct a "site:A OR site:B" string
    # We pick top 3 preferred sites to avoid query being too long/complex for DDG
    top_sites = sites[:4] 
    site_query = " OR ".join([f"site:{s}" for s in top_sites])
    
    query_1 = f"{topic} ({site_query})"
    print(f"DEBUG: Strategy 1 Query: {query_1}")
    
    results = perform_search(query_1)
    
    if results:
        # Return the top result from the targeted search
        return results[0]

    # ----------------------------------------
    # STRATEGY 2: Fallback General Search
    # ----------------------------------------
    query_2 = f"{topic} explained for beginners"
    print(f"DEBUG: Strategy 2 Query: {query_2}")
    
    results = perform_search(query_2)
    
    if results:
        # Try to prioritize preferred sites if they appear in general results
        for r in results:
            if any(s in r['url'] for s in sites):
                return r
        
        # Otherwise just return the first good result
        return results[0]

    # ----------------------------------------
    # FINAL FALLBACK (Safe)
    # ----------------------------------------
    return {
        "title": "Wikipedia article",
        "url": f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    }


