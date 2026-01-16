from docs_finder import find_best_reading
import time

def test(topic, domain):
    print(f"\n--- Testing '{topic}' ({domain}) ---")
    try:
        res = find_best_reading(topic, domain)
        print("Result:", res)
    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    test("React State", "tech")
    time.sleep(1) # Be nice to DDG
    test("Black Hole", "science")
    time.sleep(1)
    test("Inflation", "business")
    time.sleep(1)
    test("History of Rome", "general")
