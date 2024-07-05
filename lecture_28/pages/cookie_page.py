import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from lecture_28.pages.base_page import BasePage


class CookiePage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def cookie_accept_button(self):
        return self.driver.find_element(By.ID, "L2AGLb")


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://google.com")

    cookie_page = CookiePage(driver)
    cookie_page.cookie_accept_button().click()
    time.sleep(2)
