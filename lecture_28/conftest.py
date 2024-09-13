# conftest.py
import logging
import re

import pytest
from selenium import webdriver
from lecture_28.pages.cookie_page import CookiePage
from lecture_28.pages.search_page import SearchPage
from lecture_28.pages.search_result_page import SearchResultPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def open_start_page(driver):
    def _open_start_page():
        driver.get("https://google.com")

    return _open_start_page


@pytest.fixture
def accept_google_cookies(driver):
    def _accept_google_cookies():
        cookie_page = CookiePage(driver)
        cookie_page.cookie_accept_button().click()

    return _accept_google_cookies


@pytest.fixture
def search_and_submit(driver):
    def _search_and_submit(query):
        search_page = SearchPage(driver)
        search_field = search_page.search_field()
        search_button = search_page.search_button()
        search_field.clear()
        search_field.send_keys(query)
        search_button.click()

    return _search_and_submit


@pytest.fixture
def check_that_search_has_done(driver):
    def _check_that_search_has_done():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        search_result_page = SearchResultPage(driver)

        search_results = search_result_page.search_result()
        logger.debug(search_results)

        actual_res = search_results.get_attribute("wholeText")
        logger.debug(actual_res)
        # Use regex to find all digit sequences
        digits = re.findall(r"\d+", actual_res)
        logger.debug(digits)

        # Join the found sequences into a single number
        result = "".join(digits)
        logger.debug(result)

        result = int(result)
        return result > 0

    return _check_that_search_has_done
