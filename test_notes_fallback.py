from notes_generator import generate_notes

print("Testing valid URL...")
print(generate_notes("https://www.geeksforgeeks.org/django-tutorial/"))

print("\nTesting INVALID URL (should trigger fallback)...")
print(generate_notes("https://invalid-url-that-does-not-exist.com"))
