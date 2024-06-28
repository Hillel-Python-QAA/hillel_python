from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def web_element(_driver, _xpath):
    try:
        _element = WebDriverWait(_driver, timeout=5).until(
            EC.presence_of_element_located((By.XPATH, _xpath))
        )
        return _element
    except TimeoutException:
        print("За даний час елемент не зявився на сторінці")


# Ініціалізуємо драйвер браузера
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.example.com")
xpath = '//li[@id="ewuygeb"]'
element = web_element(driver, xpath)
element.click()
# Закриття браузера
driver.quit()
