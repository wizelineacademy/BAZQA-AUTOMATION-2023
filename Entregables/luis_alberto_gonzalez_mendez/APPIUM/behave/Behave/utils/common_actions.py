from utils.dictionaries.swipe_properties_text import COORDINATES

class CommonActions(object):
    def __init__(self, driver):
        self.driver = driver


    def find_element(self, *locator):
        self.driver.find_element(*locator)


    def enter_text(self, *locator, text):
        element = self.driver.find_element(*locator)
        element.send_keys(text)


    def find_and_click_element(self, *locator):
        self.driver.find_element(*locator).click()


    def assert_text(self, *locator, text):
        element_text = self.driver.find_element(*locator).text
        assert element_text == text


    def scroll(self, *locator):
        for _ in range(COORDINATES.get('MAX_NUM_OF_SWIPES')):
            try:
                self.find_and_click_element(*locator)
                break
            except:
                self.driver.swipe(COORDINATES.get('X_START'), COORDINATES.get('X_END'), COORDINATES.get('Y_START'), COORDINATES.get('Y_END'), COORDINATES.get('TIME_TO_WAIT'))
                continue
