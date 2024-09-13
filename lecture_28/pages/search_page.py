from selenium.webdriver.common.by import By

from lecture_28.pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_field(self):
        return self.driver.find_element(By.ID, "APjFqb")

    def search_button(self):
        return self.driver.find_element(
            By.XPATH, "(//input[@class='gNO89b' and @name='btnK'])[2]"
        )
