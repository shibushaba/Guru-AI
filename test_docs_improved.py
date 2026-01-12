from docs_finder import get_docs_page

def test():
    topics = ["Selenium", "Python", "Data Structures", "Java"]
    print("Testing improved docs_finder...")
    
    for topic in topics:
        print(f"\n--- Testing: {topic} ---")
        try:
            docs = get_docs_page(topic)
            print(f"Result: {docs}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test()
