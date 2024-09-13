from selenium.webdriver.common.by import By

from lecture_28.pages.base_page import BasePage


class SearchResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_result(self):
        return self.driver.find_element(By.XPATH, "//div[@id='result-stats']")
