from lecture_27.POM.src.utilities.element_actions import ElementActions


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.element = ElementActions(self.driver)
