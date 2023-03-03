from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class DetailProduct(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.store_item = (By.XPATH, "(//android.view.ViewGroup[@content-desc='store item'])[3]/android.view.ViewGroup[1]/android.widget.ImageView")
        self.name_product = (By.ANDROID_UIAUTOMATOR, '.text("Sauce Labs Bolt T-Shirt")')
        self.price = (By.XPATH, "//android.widget.TextView[@content-desc='product price']")
        self.add_car = (By.ANDROID_UIAUTOMATOR, '.text("Add To Cart")')
        self.card_badge = (By.ACCESSIBILITY_ID, "cart badge")
        self.my_cart = (By.XPATH, "//android.view.ViewGroup[@content-desc='container header']/android.widget.TextView")
        self.check_product = (By. XPATH, "//android.widget.TextView[@content-desc='product label']")
        self.check_price = (By. XPATH, "//android.widget.TextView[@content-desc='product price']")
