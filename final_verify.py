from docs_finder import find_best_reading
import time

def test_case(topic, domain, expected_term):
    print(f"\n--- Testing '{topic}' ({domain}) ---")
    try:
        res = find_best_reading(topic, domain)
        print(f"URL: {res['url']}")
        
        if expected_term in res['url']:
            print("SUCCESS")
        else:
            print(f"WARNING: Expected '{expected_term}' in URL")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    # Case 1: Direct Guess (Tech)
    test_case("Python django", "tech", "geeksforgeeks")
    time.sleep(1)
    
    # Case 2: Direct Guess (Science)
    test_case("Black Hole", "science", "britannica")
    time.sleep(1)

    # Case 3: Fallback Search (Tech - rust)
    # Rust is not in my guess list, so it should trigger general search fallback
    test_case("Rust programming", "tech", "rust-lang.org") 
    # OR any non-wiki result.
