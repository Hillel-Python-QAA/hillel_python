from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Чекаємо, доки елемент з'явиться на сторінці
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "element_id"))
)

# Чекаємо, доки елемент стане видимим на сторінці
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "element_id"))
)

# Чекаємо, доки елемент стане клікабельним на сторінці
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "element_id"))
)

# Чекаємо, доки в елементі з'явиться певний текст
element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "element_id"), "Expected Text")
)

# Чекаємо, доки заголовок сторінки містить певний текст
element = WebDriverWait(driver, 10).until(EC.title_contains("Expected Title"))
