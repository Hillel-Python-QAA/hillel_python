from bs4 import BeautifulSoup
import requests

# Завантаження HTML-сторінки
url = 'https://rtia.co.uk/'
response = requests.get(url)
html_content = response.content

# Аналіз HTML-документу з використанням BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Вилучення тексту з тегу <title> за допомогою CSS-локатора
title = soup.select_one('title').text
print("Заголовок сторінки:", title)

# Вилучення тексту з усіх тегів <a> за допомогою CSS-локатора
links = soup.select('a')
for link in links:
    # if (not link.get('href').startswith('mailto:')) and (not link.get('href').__eq__('#')):
    if link.get('href').__contains__('https'):
        print("Посилання:", link.get('href'))
