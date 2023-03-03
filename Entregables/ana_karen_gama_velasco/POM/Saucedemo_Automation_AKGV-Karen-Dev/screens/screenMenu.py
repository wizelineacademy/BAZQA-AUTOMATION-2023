from appium.webdriver.common.appiumby import AppiumBy as By

from screens.baseScreen import BaseScreen


class screenMenu(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)
        self.btn_login = (By.ACCESSIBILITY_ID, "menu item log in")

    def opcionLogin(self):
        self.driver.find_element(*self.btn_login).click()
