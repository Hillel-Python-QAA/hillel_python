# Приклад коду з тестами для pytest

import pytest
import pytest_html
from pytest_html import extras


@pytest.mark.parametrize("input_data, expected_output", [
    ([1, 2, 3], 6),
    ([-1, 0, 1], 0),
    ([10, 20, 30], 60)
])
def test_sum(input_data, expected_output):
    assert sum(input_data) == expected_output


@pytest.mark.parametrize("input_string, expected_output", [
    ("hello", "HELLO"),
    ("world", "WORLD")
])
def test_uppercase(input_string, expected_output):
    assert input_string.upper() == expected_output


def test_failed():
    assert False
