from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class CheckoutComplete(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_checkout_complete = (By.ANDROID_UIAUTOMATOR,
                                      ".text(\"Checkout Complete\")")
        self.btn_continue_shopping = (By.ACCESSIBILITY_ID,
                                      "Continue Shopping "
                                      "button")
