from docs_finder import find_best_reading
import time

print("Testing 'React' with domain 'tech'...")
try:
    res = find_best_reading("React", "tech")
    print("Result:", res)
    if any(s in res['url'] for s in ["geeksforgeeks", "w3schools", "mozilla", "tutorialspoint"]):
        print("SUCCESS: Found preferred tech site")
    elif "wikipedia" in res['url']:
        print("WARNING: Fell back to Wikipedia (acceptable if no better result)")
    else:
        print("SUCCESS: Found relevant result (non-wiki)")
except Exception as e:
    print(f"CRASH: {e}")
