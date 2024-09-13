from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def element_is_not_here(driver, element_locator: tuple[str, str], timeout=5):
    try:
        element = WebDriverWait(driver, timeout=timeout).until_not(
            EC.presence_of_element_located(element_locator)
        )
        return True
    except TimeoutException:
        print("Елемент продовжує бути на сторінці після очікуваного часу")
        return False
