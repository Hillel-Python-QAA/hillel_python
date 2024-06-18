import pytest


# Визначення фікстури з допомогою декоратора @pytest.fixture
@pytest.fixture(scope='function')
def my_fixture():
    # Ця частина коду буде виконана перед кожним тестом,
    # який використовує цю фікстуру
    data = {"key": "value"}
    yield data


# Приклад тесту, який використовує фікстуру
def test_using_fixture(my_fixture):
    # my_fixture - це аргумент, що передається в тестову функцію
    assert "key" in my_fixture
    assert my_fixture["key"] == "value"
