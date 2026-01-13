import requests
from bs4 import BeautifulSoup

def generate_notes(url):

    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    paras = soup.find_all("p")

    notes = []
    for p in paras:
        text = p.text.strip()
        if len(text) > 60 and len(notes) < 8:
            notes.append(text)

    return notes
