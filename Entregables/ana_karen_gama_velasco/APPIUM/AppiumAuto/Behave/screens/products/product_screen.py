from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class ProductScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_price_product = (By.ACCESSIBILITY_ID, "product price")
        self.lbl_name_product = (By.ANDROID_UIAUTOMATOR, ".text(\"Sauce Labs Backpack\")")
        self.btn_add_cart = (By.ACCESSIBILITY_ID, "Add To Cart button")
        self.lbl_number_cart = (By.ANDROID_UIAUTOMATOR, ".text(\"1\")")
        self.btn_cart = (By.ACCESSIBILITY_ID, "cart badge")
