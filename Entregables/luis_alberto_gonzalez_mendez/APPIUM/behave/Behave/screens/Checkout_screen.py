from appium.webdriver.common.appiumby import AppiumBy
from utils.common_actions import CommonActions

class Checkout(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.add_product1 = (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-AÑADIR A CARRITO"])[1]')
        self.add_product2 = (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-AÑADIR A CARRITO"])[2]/android.widget.TextView')
        self.tap_cart = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Carrito"]/android.view.ViewGroup/android.widget.ImageView')
        self.button_checkout = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-CHECKOUT"]')
        self.form_name = (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-Nombre"]')
        self.form_last_name = (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-Apellido"]')
        self.form_postal_code = (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-Código postal"]')
        self.button_continue = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-CONTINUAR"]/android.widget.TextView')
        self.button_terminar = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-TERMINAR"]')
        self.checkout_page = (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="test-CHECKOUT: COMPLETADO!"]/android.view.ViewGroup/android.widget.TextView[1]')