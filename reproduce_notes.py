from docs_finder import find_best_reading
from notes_generator import generate_notes

topic = "Python django"
domain = "tech"

print(f"Finding docs for '{topic}' ({domain})...")
doc = find_best_reading(topic, domain)
print("Doc Result:", doc)

print("\nGenerating notes...")
notes = generate_notes(doc['url'])
print("Notes Result:", notes)

if not notes:
    print("FAILURE: Notes are empty")
elif len(notes) == 1 and "Could not extract" in notes[0]:
    print("FAILURE: Extraction error")
else:
    print("SUCCESS: Notes generated")
