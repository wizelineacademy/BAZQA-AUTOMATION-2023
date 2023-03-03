from utils.common_actions import CommonActions
from appium.webdriver.common.appiumby import AppiumBy as By


class DataProductScreen(CommonActions):

    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_name = (By.XPATH,"//android.view.ViewGroup[@content-desc='container header']/android.widget.TextView")
        self.lbl_price = (By.ACCESSIBILITY_ID, "product price")
        self.btn_add = (By.ACCESSIBILITY_ID, "Add To Cart button")
        self.btn_cart = (By.ACCESSIBILITY_ID,"cart badge")