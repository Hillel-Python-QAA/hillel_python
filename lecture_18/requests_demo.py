import requests

# GET
url = 'http://jsonplaceholder.typicode.com/posts/1/comments'
response = requests.get(url)

# Перевірка статус-коду
if response.status_code == 200:
    data = response.json()  # отримання даних у форматі JSON
    print('Отримано дані:', data)
else:
    print('Помилка. Статус-код:', response.status_code)


# GET with params

url = 'http://jsonplaceholder.typicode.com/posts/1/comments'
params = {'postId': 1, 'email': 'Nikita@garfield.biz'}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
    print(response.request.url)
else:
    print('Помилка запиту:', response.status_code)


# POST
url = 'http://jsonplaceholder.typicode.com/posts'
data_to_send = {'userId': 10, 'id': 101, 'title': 'Some title'}

response = requests.post(url, data=data_to_send)

# Перевірка статус-коду
if response.status_code == 201:
    created_data = response.json()  # отримання даних у форматі JSON
    print('Створено дані:', created_data)
else:
    print('Помилка. Статус-код:', response.status_code)

# PUT
url = 'http://jsonplaceholder.typicode.com/posts/1'
data_to_send = {'userId': 10, 'id': 101, 'title': 'New title'}

response = requests.put(url, data=data_to_send)

# Перевірка статус-коду
if response.status_code == 200:
    updated_data = response.text  # отримання даних у форматі текст
    print('Оновлено дані:', updated_data)
else:
    print('Помилка. Статус-код:', response.status_code)

# DELETE
url = 'http://jsonplaceholder.typicode.com/posts/1'
response = requests.delete(url)

# Перевірка статус-коду
if response.status_code == 200:
    print('Дані успішно видалено')
else:
    print('Помилка. Статус-код:', response.status_code)

# Authentication

# BASIC
response = requests.get('https://api.example.com', auth=('username', 'password'))

# DIGEST
from requests.auth import HTTPDigestAuth

response = requests.get('https://api.example.com', auth=HTTPDigestAuth('username', 'password'))


# File Upload
# Відкриття файлу для завантаження
with open('file_to_upload.txt', 'rb') as file:
    files = {'file': file}

    # Виконання POST-запиту з файлом
    response = requests.post('https://example.com/upload', files=files)

# Обробка відповіді
print(response.text)

# Download
# Виконання GET-запиту для скачування файлу
response = requests.get('https://example.com/download')

# Запис файлу на диск
with open('downloaded_file.txt', 'wb') as file:
    file.write(response.content)

# SSL not verified

response = requests.get('https://your-server.com', verify=False)
print(response.text)