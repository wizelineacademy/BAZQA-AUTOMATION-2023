from selenium.common import NoSuchElementException


class BaseScreen:
    # Constructor de la clase base.
    # Define la variable de clase self.drive y le asigna el parametro driver.
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, *selector):
        return self.driver.find_element(*selector)

    #hay que cachar la excepcion que sabemos que nos va a mandar
    def elemento_es_mostrado(self, *selector):
        try:
            self.get_element(*selector) #busca el elemento
            return True
        except NoSuchElementException:
            return False