# test_google_search.py
import time

import pytest


def test_google_search_with_cookies(driver, open_start_page, accept_google_cookies, search_and_submit,
                                    check_that_search_has_done):
    open_start_page()
    time.sleep(1)
    accept_google_cookies()
    time.sleep(1)
    search_and_submit("Hillel IT School")
    time.sleep(1)
    assert check_that_search_has_done(), "No search results found"
