from duckduckgo_search import DDGS

def search_docs(topic, domain):
    print(f"Searching for '{topic}' in domain '{domain}'...")
    
    sites = []
    if domain == "tech":
        sites = ["geeksforgeeks.org", "w3schools.com", "developer.mozilla.org", "tutorialspoint.com", "freecodecamp.org"]
    elif domain == "science":
        sites = ["wikipedia.org", "britannica.com", "livescience.com", "nationalgeographic.com"]
    elif domain == "business":
        sites = ["investopedia.com", "forbes.com", "bloomberg.com", "hbr.org"]
    else:
        sites = ["wikipedia.org", "britannica.com"]
        
    # Construct site query
    site_q = " OR ".join([f"site:{s}" for s in sites])
    query = f"{topic} {site_q}"
    
    print(f"Query: {query}")
    
    try:
        results = DDGS().text(query, max_results=3)
        for r in results:
            print(f"- {r['title']}: {r['href']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_docs("React State", "tech")
    print("-" * 20)
    search_docs("Quantum Physics", "science")
