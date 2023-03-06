from appium.webdriver.common.appiumby import AppiumBy as By

from utils.common_actions import CommonActions


class HomeScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_products = (
            By.XPATH, "//android.view.ViewGroup[@content-desc='container header']/android.widget.TextView")
        self.btn_sort = (By.ACCESSIBILITY_ID, "sort button")
        self.menu_side = (By.ACCESSIBILITY_ID, "open menu")
