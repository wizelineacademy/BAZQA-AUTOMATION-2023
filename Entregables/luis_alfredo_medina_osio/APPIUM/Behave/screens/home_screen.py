from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class HomeScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_products = (By.XPATH, "//android.view.ViewGroup[@content-desc='container header']/android.widget.TextView")
        self.menu_side = (By.ACCESSIBILITY_ID, "open menu")
        self.lbl_product = (By.ANDROID_UIAUTOMATOR, '.text("Products")')
        self.btn_sort = (By.ACCESSIBILITY_ID, "sort button")
        self.lbl_ascending = (By.ANDROID_UIAUTOMATOR, '.text("Price - Ascending")')
        self.lbl_lwprice = (By.ANDROID_UIAUTOMATOR, '.text("$7.99")')

