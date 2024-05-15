import requests
from bs4 import BeautifulSoup

# Načtení HTML obsahu ze stránky
response = requests.get("https://apps.kodim.cz/python-data/dhmo")
soup = BeautifulSoup(response.text, 'html.parser')

# Výpis nadpisů všech sekcí (značka h2)
h2_headings = soup.find_all('h2')
for heading in h2_headings:
    print(heading.text)

# Výpis cest všech odkazů na stránce (značka a, atribut href)
links = soup.find_all('a')
for link in links:
    if 'href' in link.attrs:
        print(link['href'])

# Výpis cest ke všem obrázkům na stránce (značka img, atribut src)
images = soup.find_all('img')
for image in images:
    if 'src' in image.attrs:
        print(image['src'])
