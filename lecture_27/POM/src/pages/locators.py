from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.XPATH, '//username')
    PASSWORD = (By.XPATH, '//password')
    LOGIN_BUTTON = (By.XPATH, '//login_button')

