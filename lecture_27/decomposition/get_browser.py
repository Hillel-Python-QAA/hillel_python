from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def firefox(debug=False):
    # Ініціалізуємо параметри для веб-драйвера Firefox
    options = Options()
    options.add_argument("--headless")  # Запуск у безголовному режимі
    # (без відображення вікна браузера)

    # Вибираємо, чи потрібно запускати драйвер у режимі налагодження (debug mode)
    driver = webdriver.Firefox() if debug else \
        webdriver.Firefox(options=options)
    # Використання headless, якщо не включено налагодження

    # Максимізуємо вікно браузера (якщо відображення не вимкнено)
    driver.maximize_window()

    # Повертаємо об'єкт драйвера
    return driver
