from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element(driver, xpath):
    """Функція для очікування наявності елемента на сторінці"""
    try:
        element = WebDriverWait(driver, timeout=5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        raise NoSuchElementException("За даний час елемент не зявився на сторінці")


def click_element(driver, xpath):
    """Функція для кліку на елемент"""
    element = find_element(driver, xpath)
    element.click()


def fill_input(driver, xpath, text):
    """Функція для заповнення поля вводу текстом"""
    element = find_element(driver, xpath)
    element.clear()
    element.send_keys(text)
