import pytest

# Визначення фікстури, яка використовує параметр request
@pytest.fixture
def my_fixture(request):
    # Отримання ім'я поточного тесту
    test_name = request.node.name
    print('fixture name:', request.fixturename)
    print('scope:', request.scope)
    print('node:', request.node)
    print('config:', request.config)
    print(f"\nSetup for test: {test_name}")

    # Повертаємо деяні дані або ресурси, для теста
    yield "Some data"

    # Фаза teardown (очищення)
    print(f"\nTeardown for test: {test_name}")
    # Можна виконати очищення після завершення кожного тесту

# Приклад використання фікстури у тесті
def test_example(my_fixture):
    print("\nTest execution")
    # Використання даних або ресурсів, що повернулися з фікстури
    assert my_fixture == "Some data"