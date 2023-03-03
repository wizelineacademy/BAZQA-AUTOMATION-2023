from utils.common_actions import CommonActions
from appium.webdriver.common.appiumby import AppiumBy as By


class ProductDetail(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.txt_name_product = (By.XPATH, "//android.view.ViewGroup[@content-desc='container header']/android.widget.TextView")
        self.txt_price_product = (By.ACCESSIBILITY_ID, "product price")
        self.btn_add_to_cart = (By.ACCESSIBILITY_ID, "Add To Cart button")

