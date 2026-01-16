import requests
from bs4 import BeautifulSoup
import urllib.parse
import random
from duckduckgo_search import DDGS

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# (PREFERRED_SITES remains the same)
PREFERRED_SITES = {
    "tech": [
        "geeksforgeeks.org",
        "w3schools.com",
        "developer.mozilla.org",
        "tutorialspoint.com",
    ],
    "science": [
        "britannica.com",
        "nationalgeographic.com",
        "nasa.gov",
    ],
    "business": [
        "investopedia.com",
        "forbes.com",
        "bloomberg.com",
    ],
    "general": [
        "wikipedia.org",
    ]
}

def get_random_header():
    return {"User-Agent": "Mozilla/5.0"}

def perform_search(query):
    """
    Uses duckduckgo_search library to search.
    """
    try:
        results = DDGS().text(query, max_results=5)
        clean_results = []
        if results:
            for r in results:
                clean_results.append({
                    "title": r.get("title", ""),
                    "url": r.get("href", "")
                })
        return clean_results
    except Exception as e:
        print(f"DDGS Search error for '{query}': {e}")
        return []

def check_direct_url(url, title):
    try:
        # Use GET with stream=True to avoid downloading body, but behave like a normal browser request
        # HEAD requests are often blocked by WAFs (e.g. GeeksForGeeks)
        res = requests.get(url, headers=get_random_header(), timeout=5, stream=True)
        if res.status_code == 200:
            res.close() # Close connection
            return {"title": title, "url": url}
    except Exception as e:
        print(f"Direct check error for {url}: {e}")
    return None

def guess_direct_link(topic, domain):
    """
    Intelligently guesses direct links based on the domain.
    """
    topic_lower = topic.lower()
    
    # 1. Standard Slug: "python django" -> "python-django"
    slug = topic_lower.replace(" ", "-")
    
    # 2. Simplified Slug: "python django" -> "django"
    # Remove common prefixes/suffixes for better matching
    common_terms = ["python ", "javascript ", "js ", " language", " tutorial"]
    simplify_slug = topic_lower
    for term in common_terms:
        simplify_slug = simplify_slug.replace(term, "")
    
    slug_simple = simplify_slug.replace(" ", "-").strip()
    
    # 3. Clean Slug: "python django" -> "pythondjango"
    slug_clean = topic_lower.replace(" ", "")

    candidates = []

    if domain == "tech":
        # GeeksForGeeks
        # Try finding standard tutorials
        candidates.append((f"https://www.geeksforgeeks.org/{slug}/", f"{topic} - GeeksforGeeks"))
        candidates.append((f"https://www.geeksforgeeks.org/{slug}-tutorial/", f"{topic} Tutorial - GeeksforGeeks"))
        
        # Try simplified (e.g. "django" instead of "python-django")
        if slug_simple != slug:
            candidates.append((f"https://www.geeksforgeeks.org/{slug_simple}/", f"{topic} - GeeksforGeeks (Simple)"))
            candidates.append((f"https://www.geeksforgeeks.org/{slug_simple}-tutorial/", f"{topic} Tutorial (Simple)"))

        # W3Schools
        candidates.append((f"https://www.w3schools.com/{slug}/default.asp", f"{topic} - W3Schools"))
        if slug_simple != slug:
            candidates.append((f"https://www.w3schools.com/{slug_simple}/default.asp", f"{topic} - W3Schools (Simple)"))
            
        # MDN (Mozilla)
        candidates.append((f"https://developer.mozilla.org/en-US/docs/Web/{slug}", f"{topic} - MDN"))

    elif domain == "science":
        # Britannica
        candidates.append((f"https://www.britannica.com/topic/{slug}", f"{topic} - Britannica"))
        candidates.append((f"https://www.britannica.com/science/{slug}", f"{topic} - Britannica"))
        if slug_simple != slug:
            candidates.append((f"https://www.britannica.com/science/{slug_simple}", f"{topic} - Britannica (Simple)"))

    elif domain == "business":
        # Investopedia
        # Standard: /terms/i/inflation.asp
        if len(slug) > 0:
            first_char = slug[0]
            candidates.append((f"https://www.investopedia.com/terms/{first_char}/{slug}.asp", f"{topic} - Investopedia"))
            # Sometimes just slug? 
            candidates.append((f"https://www.investopedia.com/{slug}", f"{topic} - Investopedia"))

    # Try candidates
    for url, title in candidates:
        print(f"DEBUG: Guessing {url}")
        res = check_direct_url(url, title)
        if res:
            return res
            
    return None

def find_best_reading(topic, domain="general"):
    if not domain: domain = "general"

    # 1. SEARCH ENGINE LAYER
    suffix = "tutorial" if domain == "tech" else "explained"
    query = f"{topic} {suffix}"
    print(f"DEBUG: Searching '{query}'")
    
    results = perform_search(query)
    
    if results:
        preferred = PREFERRED_SITES.get(domain, PREFERRED_SITES["general"])
        # Prefer domain sites
        for r in results:
            if any(s in r['url'] for s in preferred):
                return r
        # Return top result if no preferred found
        return results[0]

    # 2. DIRECT GUESS layer (if search failed)
    print("DEBUG: Search failed, trying direct guessing...")
    direct = guess_direct_link(topic, domain)
    if direct:
        return direct
    
    # 3. ABSOLUTE FALLBACK (Browser Search)
    # If all else fails, just search the raw topic and take result #1
    print("DEBUG: Direct guess failed, trying absolute fallback search...")
    raw_results = perform_search(topic)
    if raw_results:
        # Avoid returning Wikipedia here if possible, but if it's #1, take it.
        print(f"DEBUG: Absolute fallback returning: {raw_results[0]['url']}")
        return raw_results[0]

    # 4. FINAL FALLBACK (Wikipedia)
    # Only if even the raw search returned nothing
    return {
        "title": "Wikipedia article",
        "url": f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    }
