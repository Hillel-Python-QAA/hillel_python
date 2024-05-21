# Імпортуємо необхідну бібліотеку для тестування
import unittest


# Генератор, що генерує набори тестових даних
def test_data_generator():
    test_data = [
        ([3, 2, 1], [1, 2, 3]),  # Перший набір тестових даних
        ([5, 1, 4, 2], [1, 2, 4, 5]),  # Другий набір тестових даних
        # Додати інші тестові дані тут
    ]
    for input_arr, expected_output in test_data:
        yield input_arr, expected_output


# Функція сортування, яку ми хочемо протестувати
def my_sort(arr):
    return sorted(arr)


# Клас для тестування функції сортування
class TestSortFunction(unittest.TestCase):
    # Тест для перевірки сортування
    def test_sorting(self):
        # Проходимо через кожен набір тестових даних, що генерується генератором
        for input_arr, expected_output in test_data_generator():
            # Запускаємо кожен тест як підтест, щоб забезпечити прозорість
            with self.subTest(input_arr=input_arr):
                # Перевіряємо, що функція сортування повертає очікуваний результат
                self.assertEqual(my_sort(input_arr), expected_output)


# Запускаємо тестування, якщо файл запускається напряму
if __name__ == "__main__":
    unittest.main()
