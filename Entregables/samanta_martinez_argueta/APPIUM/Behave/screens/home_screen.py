from utils.common_actions import CommonActions
from appium.webdriver.common.appiumby import AppiumBy as By


class HomeScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_products = (By.XPATH, "//android.view.ViewGroup[@content-desc='container "
                                       "header']/android.widget.TextView")
        self.menu_side = (By.ACCESSIBILITY_ID, "open menu")
        self.img_bolt_product = (By.XPATH, "(//android.view.ViewGroup[@content-desc='store item'])["
                                           "3]/android.view.ViewGroup[1]/android.widget.ImageView")
        self.btn_shop_cart = (By.ACCESSIBILITY_ID, "cart badge")
