from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class HomeScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_products = (By.XPATH, "//android.view.ViewGroup[@content-desc='container header']/android.widget.TextView")
        self.menu_side = (By.ACCESSIBILITY_ID, "open menu")
        self.sort_button = (By.ACCESSIBILITY_ID, "sort button")
        self.asc_button = (By.XPATH, "//android.view.ViewGroup[@content-desc='priceAsc']")
        self.first_element = (By.XPATH, "(//android.widget.TextView[@content-desc='store item text'])[1]")
