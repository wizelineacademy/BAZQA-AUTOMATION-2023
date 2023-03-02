from selenium.common import NoSuchElementException


class BaseScreen:
    # Constructor de la clase base.
    # Define la variable de clase self.drive y le asigna el parametro driver.
    def __init__(self, driver):
        self.driver = driver

    # obtiene cualquier elemento
    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    # Menciona si un elemento es mostrado en pantalla
    def elemento_es_mostrado(self, *locator):
        try:
            self.get_element(*locator)
            return True
        except NoSuchElementException:
            return False
