from docs_finder import find_best_reading

print("Searching for 'React'...")
try:
    res = find_best_reading("React")
    print("Result:", res)
except Exception as e:
    print("Error:", e)
