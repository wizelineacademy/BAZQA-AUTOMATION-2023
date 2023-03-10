from appium.webdriver.common.appiumby import AppiumBy as By
from Utils.common_actions import CommondActions


class SideMenuScreen(CommondActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btn_login = (By.ACCESSIBILITY_ID, "menu item log in")
