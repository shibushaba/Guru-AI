from duckduckgo_search import DDGS

def test_lib():
    print("Testing DDGS library...")
    try:
        results = DDGS().text("React tutorial site:geeksforgeeks.org", max_results=5)
        count = 0
        for r in results:
            print(f"- {r['title']}: {r['href']}")
            count += 1
        print(f"Found {count} results")
    except Exception as e:
        print(f"Library Error: {e}")

if __name__ == "__main__":
    test_lib()
