from utils.common_actions import CommonActions
from appium.webdriver.common.appiumby import AppiumBy as By


class SortBy(CommonActions):

    def __init__(self, context):
        super().__init__(context.driver)

        self.btn_priceAsc = (By.ACCESSIBILITY_ID, "priceAsc")





