from appium.webdriver.common.appiumby import AppiumBy as By

from utils.common_actions import CommonActions


class CardBadgeScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_product_name = (By.ANDROID_UIAUTOMATOR, '.text("Sauce Labs Bolt T-Shirt")')
        self.lbl_product_price = (By.ANDROID_UIAUTOMATOR, '.text("$15.99")')
        self.btn_Proceed_To_Checkout = (By.ACCESSIBILITY_ID, "Proceed To Checkout button")
