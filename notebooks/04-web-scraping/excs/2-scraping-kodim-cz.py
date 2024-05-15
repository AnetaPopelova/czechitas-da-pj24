import requests
from bs4 import BeautifulSoup

# Vytvoření session
session = requests.Session()

# Načtení webové stránky
url = "https://kodim.cz/czechitas"
response = session.get(url)

# Vytvoření instance BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')


# Hledání elementů obsahujících názvy kurzů
# Předpokládá se, že názvy kurzů jsou ve elementech se specifickou třídou
sections = soup.select(".styles_courseCard__EMR1m")

links = []
# Vypsání názvů sekcí
for section in sections:
    # Přidání atributu href (odkaz) každé sekce do seznamu links
    if 'href' in section.attrs:
        links.append(section['href'].replace('/czechitas', ''))
print(links)

# Iterace přes každý odkaz v seznamu links
for link in links:
    # Sestavení URL pro každou sekci
    section_url = url + link
    print(section_url)
    # Načtení webové stránky sekce
    section_response = session.get(section_url)
    # Vytvoření instance BeautifulSoup pro stránku sekce
    section_soup = BeautifulSoup(section_response.text, 'html.parser')
    # Hledání všech h2 elementů, předpokládá se, že tyto obsahují názvy kurzů
    titles = section_soup.select("h2")
    for title in titles:
        # Vypsání textu každého h2 elementu, což je název lekce
        print(title.text)

# Uzavření session
session.close()
