from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class SortScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btn_price_asc = (By.ACCESSIBILITY_ID, "priceAsc")
