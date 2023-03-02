class BaseScreen:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, *locator):
        return self.driver.find_element(*locator)
