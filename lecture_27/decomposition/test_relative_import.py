from .get_browser import firefox
from .processing_element import click_element, find_element, fill_input


def test_check():
    firefox()
    assert True
