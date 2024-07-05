from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class ElementActions:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: tuple[str, str]):
        """Функція для очікування наявності елемента на сторінці"""
        try:
            element = WebDriverWait(self.driver, timeout=5).until(
                EC.presence_of_element_located(locator)
            )
            self.element = element
        except TimeoutException:
            raise NoSuchElementException("За даний час елемент не з'явився на сторінці")

    def fill_input(self, text):
        """Функція для заповнення поля вводу текстом"""
        self.element.clear()
        self.element.send_keys(text)
