from youtube_finder import get_best_video
from docs_finder import get_docs_page
import sys

def test():
    print("Testing youtube_finder...")
    try:
        video = get_best_video("Selenium")
        print(f"Video: {video}")
    except Exception as e:
        print(f"Video Error: {e}")

    print("\nTesting docs_finder...")
    try:
        docs = get_docs_page("Selenium")
        print(f"Docs: {docs}")
    except Exception as e:
        print(f"Docs Error: {e}")

if __name__ == "__main__":
    test()
