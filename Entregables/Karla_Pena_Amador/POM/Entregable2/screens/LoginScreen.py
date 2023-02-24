from appium.webdriver.common.appiumby import AppiumBy as By
from screens.BaseScreen import BaseScreen


class LoginScreen(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)

        self.txtbox_username = (By.ACCESSIBILITY_ID, "Username input field")
        self.txtbox_password = (By.ACCESSIBILITY_ID, "Password input field")
        self.btn_login = (By.ACCESSIBILITY_ID, "Login button")
        self.lbl_user_required = (By.ANDROID_UIAUTOMATOR, '.text("Username is'
                                                          ' required")')
        self.lbl_credentials = (By.ANDROID_UIAUTOMATOR, '.text("Provided'
                                                        ' credentials do not'
                                                        ' match any user in'
                                                        ' this service.")')

    def login(self, username, password):

        self.driver.find_element(*self.txtbox_username).send_keys(username)
        self.driver.find_element(*self.txtbox_password).send_keys(password)
        self.driver.find_element(*self.btn_login).click()
