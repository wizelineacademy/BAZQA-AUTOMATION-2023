from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class HomeScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_products = (By.XPATH, "//android.view.ViewGroup[@content-desc='container "
                                       "header']/android.widget.TextView")
        self.menu_side = (By.ACCESSIBILITY_ID, 'open menu')
        self.first_product = (By.XPATH, "(//android.view.ViewGroup[@content-desc='store item'])[1]")
        self.btn_sort = (By.ACCESSIBILITY_ID, "sort button")
        self.lbl_price_first_product = (By.ANDROID_UIAUTOMATOR, ".text(\"$7.99\")")
        self.lbl_price_last_product = (By.ANDROID_UIAUTOMATOR, ".text(\"$49.99\")")

