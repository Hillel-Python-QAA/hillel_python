import pytest


@pytest.fixture(scope="function", autouse=True)
def my_fixture():
    print("Test start message")
    yield


class TestClass:
    def test_1(self):
        assert 1 == 1

    def test_2(self):
        assert True
