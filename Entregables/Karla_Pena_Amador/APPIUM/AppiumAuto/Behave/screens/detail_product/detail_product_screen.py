from appium.webdriver.common.appiumby import AppiumBy as By

from utils.common_actions import CommonActions


class DetailProductScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btn_product = (By.ANDROID_UIAUTOMATOR, '.text("Sauce Labs Bolt T-Shirt")')
        self.btn_add_car = (By.ACCESSIBILITY_ID, "Add To Cart button")
        self.btn_cart_badge = (By.ACCESSIBILITY_ID, "cart badge")
