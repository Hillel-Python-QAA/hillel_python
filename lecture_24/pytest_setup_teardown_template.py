import pytest


# Фікстура для налаштування
@pytest.fixture()
def database_connection():
    print("\nSetup: Connecting to the database")
    # Виконуємо підключення до бази даних
    connection = "MockDatabaseConnection"
    yield connection  # Передаємо підключення до бази даних тесту
    # Фаза teardown
    print("\nTeardown: Closing database connection")
    # Закриваємо з'єднання з базою даних
    # connection.close()


# Приклад використання фікстури у тесті
def test_database_operations(database_connection):
    print("\nTest: Performing database operations")
    # Операції з базою даних
    assert database_connection == "MockDatabaseConnection"
