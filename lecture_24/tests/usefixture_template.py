import pytest


# Використання фікстур з conftest.py на рівні класу.
@pytest.mark.usefixtures("prepare_database", "prepare_config")
class TestClassWithMultipleFixtures:
    def test_method1(self):
        print("Тестування методу 1...")

    def test_method2(self):
        print("Тестування методу 2...")
