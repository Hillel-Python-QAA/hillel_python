import pytest


# Фікстура для обробки значення параметра
@pytest.fixture
def prepare_data(request):
    data = request.param * 2
    return data


# Параметризований тест з використанням фікстури та параметра indirect
@pytest.mark.parametrize("prepare_data", [1, 2, 3], indirect=True)
def test_example(prepare_data):
    assert prepare_data % 2 == 0
