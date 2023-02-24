from appium.webdriver.common.appiumby import AppiumBy
from screens.BaseScreen import BaseScreen


class HomeScreen(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)
        self.btn_menu = (AppiumBy.ACCESSIBILITY_ID, "open menu")
        self.btn_login = (AppiumBy.ACCESSIBILITY_ID, "menu item log in")
        self.lbl_products = (AppiumBy.ANDROID_UIAUTOMATOR, '.text("Products")')

    def ir_a_login(self):
        self.driver.find_element(*self.btn_menu).click()
        self.driver.find_element(*self.btn_login).click()
