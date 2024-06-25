
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time

# Ініціалізація драйвера
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:8080/lecture_26/dialog.html")

# Показати Alert і отримати текст з нього
driver.find_element(By.XPATH, "//button[text()='Показати Alert']").click()
time.sleep(1)
alert = Alert(driver)
print("Текст Alert:", alert.text)
alert.accept()

# Показати Confirm і підтвердити його
driver.find_element(By.XPATH, "//button[text()='Показати Confirm']").click()
time.sleep(1)
alert = Alert(driver)
print("Текст Confirm:", alert.text)
alert.accept()

# Показати Prompt, ввести текст і підтвердити його
driver.find_element(By.XPATH, "//button[text()='Показати Prompt']").click()
time.sleep(1)
alert = Alert(driver)
print("Текст Prompt:", alert.text)
alert.send_keys("John")
alert.accept()

# Зачекати 2 секунди перед завершенням
time.sleep(2)

# Закрити браузер
driver.quit()
