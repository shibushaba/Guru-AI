import json
import os
import google.generativeai as genai

MEM_FILE = "memory.json"

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.0-pro")


def load_memory():
    if not os.path.exists(MEM_FILE):
        return {"topics": []}
    with open(MEM_FILE, "r") as f:
        return json.load(f)


def save_memory(mem):
    with open(MEM_FILE, "w") as f:
        json.dump(mem, f, indent=2)


def remember_topic(topic):
    mem = load_memory()
    if topic not in mem["topics"]:
        mem["topics"].append(topic)
    save_memory(mem)


def generate_practice(topic):

    prompt = f"""
Create 3 beginner-friendly practice tasks for learning:
{topic}

They should be simple and actionable.
"""

    res = model.generate_content(prompt).text
    return [r for r in res.split("\n") if len(r.strip()) > 5]
