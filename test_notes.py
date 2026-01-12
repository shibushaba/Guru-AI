from notes_generator import generate_notes

def test():
    print("Testing notes_generator...")
    url = "https://www.geeksforgeeks.org/?s=Selenium"
    try:
        notes = generate_notes(url)
        print(f"Notes count: {len(notes)}")
        for i, n in enumerate(notes):
            print(f"{i+1}. {n[:100]}...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test()
