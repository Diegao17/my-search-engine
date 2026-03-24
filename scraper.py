import requests
from bs4 import BeautifulSoup
import json

headers = {
    "User-Agent": "Mozilla/5.0"
}

urls = [
    "https://en.wikipedia.org/wiki/Minecraft",
    "https://en.wikipedia.org/wiki/The_Legend_of_Zelda",
    "https://en.wikipedia.org/wiki/Grand_Theft_Auto_V",
    "https://en.wikipedia.org/wiki/Fortnite",
    "https://en.wikipedia.org/wiki/Call_of_Duty",
    "https://en.wikipedia.org/wiki/League_of_Legends",
    "https://en.wikipedia.org/wiki/Overwatch",
    "https://en.wikipedia.org/wiki/Red_Dead_Redemption_2",
    "https://en.wikipedia.org/wiki/Elden_Ring",
    "https://en.wikipedia.org/wiki/Dark_Souls",
    "https://en.wikipedia.org/wiki/Resident_Evil",
    "https://en.wikipedia.org/wiki/Halo_(franchise)",
    "https://en.wikipedia.org/wiki/Assassin%27s_Creed",
    "https://en.wikipedia.org/wiki/Counter-Strike",
    "https://en.wikipedia.org/wiki/Valorant",
    "https://en.wikipedia.org/wiki/Super_Mario",
    "https://en.wikipedia.org/wiki/Animal_Crossing",
    "https://en.wikipedia.org/wiki/Final_Fantasy",
    "https://en.wikipedia.org/wiki/Street_Fighter",
    "https://en.wikipedia.org/wiki/Madden_NFL_26",
    "https://en.wikipedia.org/wiki/EA_Sports_FC_26",
    "https://es.wikipedia.org/wiki/Videojuegos_de_Fórmula_1",
    "https://en.wikipedia.org/wiki/Sonic_Frontiers",
    "https://en.wikipedia.org/wiki/Ghost_of_Tsushima"
]

corpus = []

for i, url in enumerate(urls):
    print(f"Scraping: {url}")

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # 🔹 Manejo seguro del título
        title_tag = soup.find("h1")
        title = title_tag.text if title_tag else f"Document {i+1}"

        # 🔹 Extraer texto
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs]).strip()

        if len(text.split()) < 50:
            print("Texto muy corto, saltando...")
            continue

        corpus.append({
            "id": i + 1,
            "title": title,
            "text": text[:2000],
            "source": url
        })

    except Exception as e:
        print(f"Error en {url}: {e}")

with open("corpus.json", "w", encoding="utf-8") as f:
    json.dump(corpus, f, indent=2, ensure_ascii=False)

print("Corpus generado ✅")