from appium.webdriver.common.touch_action import TouchAction
from utils.dictionaries.touch_data import DATA_TOUCH
class CommonActions(object):
    def __init__(self, driver):
        self.driver = driver
        self.touch = TouchAction(self.driver)
#metodos

    def  find_element(self, *locator):
        return self.driver.find_element(*locator)

    def assert_text(self, *locator, text):
        element_text = self.find_element(*locator).text
        assert element_text == text

    def tap_element(self, *locator):
        self.touch.tap(self.find_element(*locator)).perform()

    def fill_text(self, *locator, text):
        text_field = self.find_element(*locator)
        text_field.send_keys(text)

    def swap_screen(self):
        self.touch.press(None, DATA_TOUCH['X_POINT_START'], DATA_TOUCH['Y_POINT_START']).wait(DATA_TOUCH['WAIT_MILLISECONDS']).move_to(None,DATA_TOUCH ['X_POINT_START'], DATA_TOUCH['Y_POINT_END'])             .release().perform()
