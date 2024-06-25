from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Ініціалізація веб-драйвера для Chrome
driver = webdriver.Chrome()
driver.maximize_window()
# Відкриття веб-сторінки
driver.get("http://0.0.0.0:8080/demo.html")

# Робота з веб-елементами і виконання дій на сторінц
# ID
user_field = driver.find_element(By.ID, 'username')
pass_field = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.ID, 'login_button')
# # XPath
# user_field = driver.find_element(By.XPATH, "//input[@id='username']")
# pass_field = driver.find_element(By.XPATH, "//input[@id='password']")
# login_button = driver.find_element(By.XPATH, "//button[@id='login_button']")
# # CSS Selector
# user_field = driver.find_element(By.CSS_SELECTOR, ".input-field#username")
# pass_field = driver.find_element(By.CSS_SELECTOR, ".input-field#password")
# login_button = driver.find_element(By.CSS_SELECTOR, "#login_button")
user_field.send_keys("UserName")
sleep(1)
pass_field.send_keys("Password")
sleep(1)
login_button.click()
sleep(1)

# Закриття браузера
driver.quit()
