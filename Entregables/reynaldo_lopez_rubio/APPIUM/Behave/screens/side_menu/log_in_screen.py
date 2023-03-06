from appium.webdriver.common.appiumby import AppiumBy as By
from Utils.common_actions import CommondActions


class LogInScreen(CommondActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.txt_username = (By.ACCESSIBILITY_ID, "Username input field")
        self.txt_password = (By.ACCESSIBILITY_ID, "Password input field")
        self.btn_login = (By.ACCESSIBILITY_ID, "Login button")

    def __login__(self, context):
        self.fill_text(*self.txt_username, text=context.STANDARD_USER)
        self.fill_text(*self.txt_password, text=context.PASSWORD)
        self.tap_element(*self.btn_login)