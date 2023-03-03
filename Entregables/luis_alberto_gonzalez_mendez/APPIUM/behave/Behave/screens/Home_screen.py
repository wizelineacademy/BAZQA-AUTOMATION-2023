from appium.webdriver.common.appiumby import AppiumBy
from utils.common_actions import CommonActions

class HomeScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.tap_product = (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-Articulo"])[1]/android.view.ViewGroup/android.widget.ImageView')
        self.product_price = (AppiumBy.ACCESSIBILITY_ID, 'test-Precio')
        self.product_name = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Descripción"]/android.widget.TextView[1]')
