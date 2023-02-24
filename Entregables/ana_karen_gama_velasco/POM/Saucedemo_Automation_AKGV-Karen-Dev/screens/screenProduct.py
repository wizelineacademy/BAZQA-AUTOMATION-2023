from appium.webdriver.common.appiumby import AppiumBy as By

from screens.baseScreen import BaseScreen


class screenProduct(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)
        self.btn_menu = (By.ACCESSIBILITY_ID, "open menu")
        self.lbl_productos = (By.ANDROID_UIAUTOMATOR, '.text("Products")')

    def abrirMenu(self):
        self.driver.find_element(*self.btn_menu).click()
