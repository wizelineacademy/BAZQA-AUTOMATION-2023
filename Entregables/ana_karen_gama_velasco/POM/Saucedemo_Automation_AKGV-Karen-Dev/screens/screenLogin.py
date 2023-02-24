from appium.webdriver.common.appiumby import AppiumBy as By
from screens.baseScreen import BaseScreen


class screenLogin(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)
        self.txtbox_username = (By.ACCESSIBILITY_ID, "Username input field")
        self.txtbox_password = (By.ACCESSIBILITY_ID, "Password input field")
        self.btn_login = (By.ACCESSIBILITY_ID, "Login button")
        self.lbl_dismatch = (By.ANDROID_UIAUTOMATOR, ".text(\"Provided"
                                                     " credentials do"
                                                     " not match any user "
                                                     "in this service.\") ")
        self.lbl_nousername = (By.ACCESSIBILITY_ID, "Username-error-message")
        self.lbl_nopassword = (By.ANDROID_UIAUTOMATOR, ".text(\"Password"
                                                       " is required\")")

    def login(self, username, password):
        self.driver.find_element(*self.txtbox_username).send_keys(username)
        self.driver.find_element(*self.txtbox_password).send_keys(password)
        self.driver.find_element(*self.btn_login).click()
