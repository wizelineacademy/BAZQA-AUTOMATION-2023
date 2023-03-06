from appium.webdriver.common.appiumby import AppiumBy as By

from utils.common_actions import CommonActions


class SortProductScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btn_price_asc = (By.ACCESSIBILITY_ID, "priceAsc")
        self.lbl_higher_price = (By.ANDROID_UIAUTOMATOR, '.text("$49.99")')
        self.lbl_lower_price = (By.ANDROID_UIAUTOMATOR, '.text("$7.99")')
