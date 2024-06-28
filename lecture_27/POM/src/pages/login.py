from lecture_27.POM.src.pages.base_page import BasePage
from lecture_27.POM.src.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators
        self.username_field = self.element.find_element(self.locators.USERNAME)
        self.password_field = self.element.find_element(self.locators.PASSWORD)
        self.login_button = self.element.find_element(self.locators.LOGIN_BUTTON)

    def login(self, username, password):
        self.username_field.fill_input(username)
        self.password_field.fill_input(password)
        self.login_button.click()
