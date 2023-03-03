from appium.webdriver.common.touch_action import TouchAction

class CommonActions(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator) #se le agregó return para ocuparlo en los otros métodos

    def assert_text(self, *locator, text):
        element_text = self.find_element(*locator).text
        assert element_text == text

    def tap_element(self, *locator):
        action = TouchAction(self.driver)
        action.tap(self.find_element(*locator)).perform() #perform es para indicar que ejecute la acción

    def fill_text(self, *locator, text):# se agrega text porque vamos a ingresar texto
        text_field = self.find_element(*locator)
        text_field.send_keys(text)


