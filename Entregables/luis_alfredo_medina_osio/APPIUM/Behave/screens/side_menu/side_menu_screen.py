from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class SideMenuScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btn_login = (By.ACCESSIBILITY_ID, "menu item log in")
