from appium.webdriver.common.appiumby import AppiumBy
from utils.common_actions import CommonActions


class PriceFilter(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.tap_filter = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Modal Selector Button"]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView')
        self.price_filter = (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="Selector container"]/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.TextView')
        self.lower_price = (AppiumBy.XPATH, '(//android.widget.TextView[@content-desc="test-Precio"])[1]')
        self.name_product = (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="test-PRODUCTOS"]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView[3]')
        self.higher_price = (AppiumBy.XPATH, '(//android.widget.TextView[@content-desc="test-Precio"])[4]')
