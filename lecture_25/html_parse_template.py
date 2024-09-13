from lxml import html
import requests

# Завантаження HTML-сторінки
url = "https://rtia.co.uk/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}
response = requests.get(url, headers=headers, timeout=5)
print(response.status_code)
html_content = response.content

# Аналіз HTML-документу з використанням lxml
tree = html.fromstring(html_content)

# Вилучення тексту з тегу <title>
title = tree.findtext(".//title")
print("Заголовок сторінки:", title)

# Вилучення всіх посилань з тегу <a>
links = set(tree.xpath(".//a/@href"))
for link in links:
    print("Посилання:", link)
