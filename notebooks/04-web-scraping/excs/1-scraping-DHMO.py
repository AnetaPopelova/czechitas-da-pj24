from requests_html import HTMLSession

"""
Napište program, který bude pracovat se stránkou o DHMO na adrese https://apps.kodim.cz/python-data/dhmo.
"""
session = HTMLSession()
stranka = session.get("https://apps.kodim.cz/python-data/dhmo")

# Nechť program vypíše na výstup nadpisy všech sekcí (značka h2).
# for nadpis in stranka.html.find("h2"):
#     print(nadpis.text)

# Nechť program vypíše na výstup cesty všech odkazů na stránce (značka a, atribut href).
# for odkaz in stranka.html.find("a"):
#     print(odkaz.attrs["href"])

# # Nechť program vypíše na výstup cesty ke všem obrázkům na stránce (značka img, atribut src).
for obrazek in stranka.html.find("img"):
    print(obrazek.attrs["src"])

# session.close()
