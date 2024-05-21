import unittest
import requests


def get_data_from_api():
    # Функція для виконання запиту до API та отримання даних
    response = requests.get("https://api.example.com/data")
    return response.json()


class TestAPI(unittest.TestCase):
    def test_api_response(self):
        # Тест для перевірки відповіді API
        api_data = get_data_from_api()  # Отримуємо дані з API
        self.assertIsInstance(api_data, list)  # Перевіряємо, що отримані дані є списком
        for item in api_data:
            # Проходимо через кожен елемент отриманих даних
            self.assertIn("id", item)  # Перевіряємо, що кожен елемент містить ключ "id"
            self.assertIn("name", item)  # Перевіряємо, що кожен елемент містить ключ "name"
            # Додаткові перевірки можна додати тут


if __name__ == "__main__":
    unittest.main()
