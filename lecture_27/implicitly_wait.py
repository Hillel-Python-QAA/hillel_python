from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_example_with_implicit_wait(browser):
    browser.implicitly_wait(10)  # Чекати не більше 10 секунд

    browser.get("https://www.example.com")

    # Знаходимо елемент на сторінці
    heading = browser.find_element(By.TAG_NAME, "h1")

    # Перевіряємо, чи вірний текст заголовку
    assert heading.text == "Example Domain"


def test_example_with_explicit_wait(browser):
    browser.get("https://www.example.com")

    # Чекаємо, поки заголовок сторінки з'явиться (не більше 10 секунд)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )

    # Знаходимо елемент на сторінці після очікування
    heading = browser.find_element(By.TAG_NAME, "h1")

    # Перевіряємо, чи вірний текст заголовку
    assert heading.text == "Example Domain"
