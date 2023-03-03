from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class CartScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_price_product = (By.ACCESSIBILITY_ID, "product price")
        self.lbl_name_product = (By.ACCESSIBILITY_ID, "product label")
        self.btn_check_out = (By.ACCESSIBILITY_ID, "Proceed To Checkout button")
