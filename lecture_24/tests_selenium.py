import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_PAGE_URL = "http://127.0.0.1:8080/search.html"


# Клас Page Object для головної сторінки
class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = driver.find_element(By.ID, "searchQuery")
        self.search_button = driver.find_element(By.ID, "searchButton")

    def search_for(self, query):
        self.search_box.clear()
        self.search_box.send_keys(query)
        self.search_button.click()


# Клас для тестування пошуку на головній сторінці
class TestSearch:
    @pytest.fixture(scope="class")
    def browser(self):
        # Ініціалізація веб-драйвера
        driver = webdriver.Chrome()
        driver.maximize_window()
        # Відкриття головної сторінки
        driver.get(SEARCH_PAGE_URL)
        yield driver
        # Завершення роботи веб-драйвера
        driver.quit()

    @pytest.mark.parametrize("query", ["python", "pytest", "selenium"])
    def test_search(self, browser, query):
        # Створення екземпляра Page Object для головної сторінки
        main_page = MainPage(browser)
        # Виконання пошуку з використанням запиту
        main_page.search_for(query)
        # Очікування завантаження результатів пошуку
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "searchResults"))
        )
        # Перевірка результатів пошуку
        search = browser.find_elements(By.TAG_NAME, "td")
        print([res.text for res in search])
        assert any(query in res.text for res in search), 'Query not found'
        time.sleep(2)
