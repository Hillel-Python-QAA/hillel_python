from lxml import html
import requests

# Завантаження HTML-сторінки
url = 'https://rtia.co.uk/'
response = requests.get(url)
html_content = response.content

# Парсинг HTML-документу з використанням XPath
tree = html.fromstring(html_content)

# Вилучення тексту з тегу <title> за допомогою XPath
title = tree.xpath('//title/text()')[0]
print("Заголовок сторінки:", title)

# Вилучення тексту з усіх тегів <a> за допомогою XPath
links = tree.xpath('//a/text()')
for link in links:
    print("Посилання:", link)

# Відносний шлях
# //*[@id="get-in-touch-wrap"]/div/a

# //a[contains(text(), 'Contact us now')]

# Абсолютний шлях
# /html/body/div[1]/div[4]/div[6]/div/div/a
