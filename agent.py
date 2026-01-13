from youtube_finder import get_best_video
from docs_finder import find_best_reading
from notes_generator import generate_notes
from utils import remember_topic, generate_practice


def agent_execute(topic, mode, domain):

    remember_topic(topic)

    video = get_best_video(topic, mode)
    reading = find_best_reading(topic)
    notes = generate_notes(reading["url"]) if reading else []
    practice = generate_practice(topic)

    intro = (
        f"You selected **{mode.upper()} learning** for a **{domain.upper()} topic**.\n"
        f"Let's learn **{topic}** step by step."
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
