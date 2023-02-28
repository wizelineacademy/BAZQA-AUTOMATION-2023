from selenium.common import NoSuchElementException


class BaseScreen:
    # Define la variable de clase self.drive y le asigna el parametro driver.
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def elemento_es_mostrado(self, *locator):
        try:
            self.get_element(*locator)
            return True
        except NoSuchElementException:
            return False
