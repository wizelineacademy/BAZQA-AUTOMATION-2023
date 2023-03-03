from utils.common_actions import CommonActions
from appium.webdriver.common.appiumby import AppiumBy as By


class MyCart(CommonActions):

    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_name1 = (By.ACCESSIBILITY_ID, "product label")
        self.lbl_price1 = (By.ACCESSIBILITY_ID, "product price")