from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Ініціалізація драйвера
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:8080/lecture_26/elements.html")

# Знаходження текстових полів за ID і введення тексту
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("example_username")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("example_password")

# Знаходження радіо кнопок за ID і вибір варіанта
male_radio = driver.find_element(By.ID, "female")
male_radio.click()

# Знаходження чекбоксу за ID і встановлення прапорця
newsletter_checkbox = driver.find_element(By.ID, "newsletter")
newsletter_checkbox.click()

# Вибір значення з випадаючого списку за ID
country_dropdown = Select(driver.find_element(By.ID, "country"))
country_dropdown.select_by_visible_text("США")

# Натискання на кнопку за ID
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

# Зачекати 5 секунд перед завершенням
time.sleep(5)

# Закрити браузер
driver.quit()
