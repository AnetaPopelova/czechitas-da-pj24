# pip3 install requests-html

from requests_html import HTML

with open(
    "ukazka.html",
    encoding="utf-8",
) as soubor:
    obsah = soubor.read()
html = HTML(html=obsah)

for odstavec in html.find("p"):
    print(odstavec.text)
