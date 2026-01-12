from duckduckgo_search import DDGS
import time

def get_docs_page(topic):
    # Search for the best documentation across the web using DuckDuckGo
    # User prefers "single page" tutorials like W3Schools, JavaTpoint, GFG
    query = f"{topic} tutorial w3schools javatpoint geeksforgeeks"
    print(f"Searching web for: {query}")
    
    preferred_domains = [
        "w3schools.com",
        "javatpoint.com",
        "geeksforgeeks.org",
        "tutorialspoint.com",
        "programiz.com",
        "freecodecamp.org",
        "mozilla.org" # MDN is also great
    ]

    try:
        results = DDGS().text(query, max_results=10, backend="lite")
        
        # unique results
        seen_urls = set()
        candidates = []

        for r in results:
            href = r.get("href", "")
            if href in seen_urls: continue
            seen_urls.add(href)
            
            # Filter out unwanted
            if any(x in href for x in ["youtube.com", "vimeo.com", "facebook.com", "twitter.com", "reddit.com", "stackoverflow.com", "stackexchange.com"]):
                continue
            if href.endswith(".pdf"):
                continue

            candidates.append(href)
            
            # Check for preferred domains immediately
            for domain in preferred_domains:
                if domain in href:
                    return href
        
        # If no preferred domain found, return the first valid candidate
        if candidates:
            return candidates[0]
            
        # Fallback if no results found
        return f"https://duckduckgo.com/?q={topic}+tutorial"

    except Exception as e:
        print(f"Error searching web text: {e}")
    
    # Fallback to Chat if Text search fails (often robust against some blocks)
    try:
        print("Trying fallback to chat...")
        results = DDGS().chat(f"give me the best documentation url for {topic}", model='gpt-4o-mini') 
        # The result is a string, we need to extract a URL or it might be just text.
        # Chat is tricky because it returns text. Let's stick to text search with retries or alternative backend.
        pass
    except:
        pass

    # Simple fallback: Return a google search URL
    return f"https://www.google.com/search?q={topic}+documentation"