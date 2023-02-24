from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from screens.BaseScreen import BaseScreen


class LoginPage(BaseScreen):

    NAME_USER = (AppiumBy.ACCESSIBILITY_ID, 'test-Usuario')
    NAME_PASS = (AppiumBy.ACCESSIBILITY_ID, 'test-Contraseña')
    NAME_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'test-LOGIN')
    GET_ERROR = (AppiumBy.XPATH,
                 '//android.view.ViewGroup[@content-desc="test-Error"]/'
                 'android.widget.TextView')
    GET_HOME = (AppiumBy.ANDROID_UIAUTOMATOR, '.text("PRODUCTOS")')

    def __int__(self, driver):
        super().__init__(driver)

    def Login(self, username, password):
        self.get_element(*self.NAME_USER).click()
        self.get_element(*self.NAME_USER).send_keys(username)
        self.get_element(*self.NAME_PASS).click()
        self.get_element(*self.NAME_PASS).send_keys(password)
        self.get_element(*self.NAME_BUTTON).click()

    def is_login_successful(self):
        try:
            get_error = self.get_element(*self.GET_ERROR)
            return get_error.text
        except NoSuchElementException:
            get_home = self.get_element(*self.GET_HOME)
            return get_home.text
