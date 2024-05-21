# Імпортуємо необхідні бібліотеки
import unittest
import requests


# Генератор для отримання даних з API
def api_data_generator():
    response = requests.get("https://api.example.com/data")
    for item in response.json():
        yield item


# Клас для тестування відповіді API
class TestAPI(unittest.TestCase):
    # Тест для перевірки відповіді API
    def test_api_response(self):
        # Проходимо через кожен елемент, що генерується генератором
        for item in api_data_generator():
            # Перевіряємо, чи є отриманий елемент словником
            self.assertIsInstance(item, dict)
            # Перевіряємо наявність ключів "id" і "name"
            self.assertIn("id", item)
            self.assertIn("name", item)
            # Додаткові перевірки можна додати тут


# Запускаємо тестування, якщо файл запускається напряму
if __name__ == "__main__":
    unittest.main()
