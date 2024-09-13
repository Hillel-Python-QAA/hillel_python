import pytest


def add(x, y):
    return x + y


@pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (5, 5, 10), (10, -5, 5)])
def test_addition(x, y, expected):
    result = add(x, y)
    assert result == expected
