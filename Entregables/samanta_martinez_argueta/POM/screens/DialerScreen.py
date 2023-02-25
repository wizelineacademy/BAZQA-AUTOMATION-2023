from appium.webdriver.common.appiumby import AppiumBy

from screens.BaseScreen import BaseScreen


# PageObject Dialer
class DialerScreen(BaseScreen):
    # Variables de clase. Elementos Digit y Digit field.
    DIGIT = 'com.android.dialer:id/%s'
    DIGIT_FIELD = "com.android.dialer:id/digits"

    # Constructor de clase. Llama al constructor de la clase base, para asignarle la variable driver
    def __int__(self, driver):
        super().__init__(driver)

    # Método de clase. Acción de dar click a un número.
    def click_digit(self, digit):
        digit_locator = self.DIGIT % digit
        self.driver.find_element(by=AppiumBy.ID, value=digit_locator).click()

    # Método de clase. Acción de obtener el texto del elemento input digits
    def get_input_digits(self):
        digit_field = self.driver.find_element(by=AppiumBy.ID, value=self.DIGIT_FIELD)
        return digit_field.get_attribute('text')
