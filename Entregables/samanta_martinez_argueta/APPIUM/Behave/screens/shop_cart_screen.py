from utils.common_actions import CommonActions
from appium.webdriver.common.appiumby import AppiumBy as By


class ShoppingCart(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btn_cart = (By.ACCESSIBILITY_ID, "cart badge")
        self.lbl_my_cart = (
            By.XPATH, "//android.view.ViewGroup[@content-desc='container header']/android.widget.TextView")
        self.lbl_name_bolt = (By.ACCESSIBILITY_ID, "product label")
        self.lbl_price_bolt = (By.ACCESSIBILITY_ID, "product price")

