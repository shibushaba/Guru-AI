import requests
from bs4 import BeautifulSoup

def generate_notes(doc_url):
    res = requests.get(doc_url)
    soup = BeautifulSoup(res.text, "html.parser")

    paras = soup.find_all("p")

    notes = []
    for p in paras:
        text = p.text.strip()
        if len(text) > 40 and len(notes) < 8:
            notes.append(text)

    return notes    