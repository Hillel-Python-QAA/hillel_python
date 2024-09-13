import pytest


# Припустимо, що у нас є кілька фіктивних фікстур для підготовки тестового середовища.
@pytest.fixture(scope="class")
def prepare_database():
    print("Підготовка бази даних...")
    yield
    print("Очищення бази даних...")


@pytest.fixture(scope="class")
def prepare_config():
    print("Підготовка конфігурації...")
    yield
    print("Очищення конфігурації...")
