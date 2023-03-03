from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class CheckoutReview(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btn_place_order = (By.ACCESSIBILITY_ID,
                                "Place Order button")
