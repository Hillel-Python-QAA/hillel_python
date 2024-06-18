import pytest


# Визначення фікстури з параметром params
@pytest.fixture(params=[1, 2, 3])
def my_fixture(request):
    param_value = request.param
    print(f"Setup with param value: {param_value}")
    return param_value * 2


# Приклад використання фікстури у тесті
def test_using_fixture(my_fixture):
    print(f"Test with fixture value: {my_fixture}")
    assert my_fixture % 2 == 0
