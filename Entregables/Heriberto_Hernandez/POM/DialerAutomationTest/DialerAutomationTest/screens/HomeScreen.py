
from DialerAutomationTest.screens.BaseScreen import BaseScreen
from appium.webdriver.common.appiumby import AppiumBy as By


class HomeScreen(BaseScreen):
    def __init__(self, driver):
        super().__init__(driver)
        self.btn_menu = (By.ACCESSIBILITY_ID, "open menu")
        self.btn_login = (By.ACCESSIBILITY_ID, "menu item log in")
        self.lbl_products = (By.ANDROID_UIAUTOMATOR,'.text("Products")')

    #Metodo permite ingresar  los datos en la pantalla de login
    def go_to_login(self):
        self.driver.find_element(*self.btn_menu).click()
        self.driver.find_element(*self.btn_login).click()

