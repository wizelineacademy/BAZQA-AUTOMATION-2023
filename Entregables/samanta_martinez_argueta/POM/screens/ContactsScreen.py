from appium.webdriver.common.appiumby import AppiumBy

from screens.BaseScreen import BaseScreen


# PageObject Contacts
class ContactsScreen(BaseScreen):
    # Variable de clase. Elemento Key Pad.
    KEY_PAD = "key pad"

    # Constructor de clase. Llama al constructor de la clase base, para asignarle la variable driver
    def __int__(self, driver):
        super().__init__(driver)

    # Método de clase. Accion de desplegar el key pad.
    def open_key_pad(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=self.KEY_PAD).click()
