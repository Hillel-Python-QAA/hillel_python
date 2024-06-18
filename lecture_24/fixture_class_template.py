import pytest


class TestClass:

    @pytest.fixture(scope="class")
    def my_fixture(self):
        data = {"key": "value"}
        print('Use of the fixture')
        yield data

    def test_1(self, my_fixture):
        print("Test 1 is using the fixture")
        assert "key" in my_fixture
        assert my_fixture["key"] == "value"

    def test_2(self, my_fixture):
        print("Test 2 is using the fixture")
        assert "key" in my_fixture
        assert my_fixture["key"] == "value"
