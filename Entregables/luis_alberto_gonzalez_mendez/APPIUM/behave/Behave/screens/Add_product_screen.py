from appium.webdriver.common.appiumby import AppiumBy
from utils.common_actions import CommonActions

class AddProduct(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.add_product = (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-AÑADIR A CARRITO"])[2]')
        self.tap_car = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Carrito"]/android.view.ViewGroup/android.view.ViewGroup')
        self.price_product = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Precio"]/android.widget.TextView')
        self.name_product = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Descripción"]/android.widget.TextView[1]')
