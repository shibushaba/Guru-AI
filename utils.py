import json
import os

MEM_FILE = "memory.json"


# ---------------------------
# 🧠 MEMORY SYSTEM
# ---------------------------

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


# ---------------------------
# 🛠 PRACTICE GENERATOR (AGENTIC)
# ---------------------------

def generate_practice(topic):

    t = topic.lower()

    # ---- TECH PRACTICE ----
    if any(k in t for k in ["python", "pandas", "java", "react", "django", "api", "sql", "selenium"]):
        return [
            f"Install required tools and set up environment for {topic}.",
            f"Write a small program or script related to {topic}.",
            f"Modify an example project and observe the result."
        ]

    # ---- SCIENCE PRACTICE ----
    if any(k in t for k in ["physics", "chemistry", "biology", "cell", "atom", "gravity", "photosynthesis"]):
        return [
            f"Draw a simple diagram explaining {topic}.",
            f"Explain {topic} in your own words in 5 sentences.",
            f"Find a real-life example where {topic} is applied."
        ]

    # ---- BUSINESS / FINANCE PRACTICE ----
    if any(k in t for k in ["stock", "market", "finance", "economy", "crypto", "business", "marketing"]):
        return [
            f"Read one current news article related to {topic}.",
            f"Write 3 advantages and 3 risks of {topic}.",
            f"Explain how {topic} affects normal people."
        ]

    # ---- GENERAL LEARNING PRACTICE ----
    return [
        f"Summarize {topic} in 5 bullet points.",
        f"Teach {topic} to a friend or in front of a mirror.",
        f"Search for one real-world application of {topic}."
    ]
