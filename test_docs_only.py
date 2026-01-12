from docs_finder import get_docs_page

def test():
    print("Testing docs_finder...")
    try:
        docs = get_docs_page("Selenium")
        print(f"Docs: {docs}")
    except Exception as e:
        print(f"Docs Error: {e}")

if __name__ == "__main__":
    test()
