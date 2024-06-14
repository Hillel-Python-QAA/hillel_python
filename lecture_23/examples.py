import requests


BASE_URL = "https://qauto.forstudy.space/api"
response = requests.get(f"{BASE_URL}")
response = requests.post(f"{BASE_URL}")
response = requests.put(f"{BASE_URL}")
response = requests.delete(f"{BASE_URL}")


headers = {'Content-Type': 'application/json'}
response = requests.get(f"{BASE_URL}", headers=headers)

params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get(f"{BASE_URL}", params=params, headers=headers)


# Dataform

payload = 'key1=value1&key2=value2'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.get(f"{BASE_URL}", headers=headers, data=payload, timeout=5)

payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get(f"{BASE_URL}", headers=headers, data=payload, timeout=5)

# JSON
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get(f"{BASE_URL}", headers=headers, json=payload, timeout=5)


# Binary data
# Відкриваємо файл зображення у бінарному режимі для читання
with open('image.jpg', 'rb') as file:
    # Читаємо дані з файлу
    image_data = file.read()

# Виконуємо HTTP POST-запит, передаючи дані у бінарному форматі
response = requests.post('<https://api.example.com/upload_image>', data=image_data)

