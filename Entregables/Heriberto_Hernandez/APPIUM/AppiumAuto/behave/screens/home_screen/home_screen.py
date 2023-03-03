from utils.common_actions import CommonActions
from appium.webdriver.common.appiumby import AppiumBy as By


class HomeScreen(CommonActions):

    def __init__(self, context):

        super().__init__(context.driver)
        self.lbl_products = (By.XPATH,"//android.view.ViewGroup[@content-desc='container header']/android.widget.TextView")
        self.menu_side = (By.ACCESSIBILITY_ID,"open menu")
        self.lbl_product1 = (By.XPATH,"(//android.view.ViewGroup[@content-desc='store item'])[1]/android.view.ViewGroup[1]")
        self.sort_button = (By.ACCESSIBILITY_ID, "sort button")
