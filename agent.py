from youtube_finder import get_best_video
from docs_finder import find_best_reading
from notes_generator import generate_notes
from utils import remember_topic, generate_practice


def agent_execute(topic, mode, domain):

    # -------------------
    # MEMORY
    # -------------------
    remember_topic(topic)

    # -------------------
    # VIDEO (SAFE)
    # -------------------
    video = None
    try:
        video = get_best_video(topic, mode)
    except Exception as e:
        print("Video fetch failed:", e)
        video = None

    if not video:
        video = {
            "title": "Search on YouTube for: " + topic,
            "url": f"https://www.youtube.com/results?search_query={topic.replace(' ', '+')}+tutorial"
        }

    # -------------------
    # READING (SAFE)
    # -------------------
    reading = None
    try:
        reading = find_best_reading(topic, domain)
    except Exception as e:
        print("Reading fetch failed:", e)
        reading = None

    if not reading:
        reading = {
            "title": "Wikipedia article",
            "url": f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
        }

    # -------------------
    # NOTES (SAFE)
    # -------------------
    notes = []
    try:
        notes = generate_notes(reading["url"])
    except Exception as e:
        print("Notes generation failed:", e)
        notes = ["Read the article and summarize key points in your own words."]

    # -------------------
    # PRACTICE (RULE BASED)
    # -------------------
    practice = generate_practice(topic)

    # -------------------
    # INTRO MESSAGE
    # -------------------
    intro = (
        f"You selected **{mode.upper()} learning** for a **{domain.upper()} topic**.\n\n"
        f"Here is a focused learning pack for **{topic}**."
    )

    return {
        "topic": topic,
        "mode": mode,
        "domain": domain,
        "message": intro,
        "video": video,
        "reading": reading,
        "notes": notes,
        "practice": practice
    }
