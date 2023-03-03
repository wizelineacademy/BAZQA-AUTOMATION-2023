from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class CartScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_product = (By.ANDROID_UIAUTOMATOR, '.text("Sauce Labs Fleece Jacket")')
        self.lbl_jacket = (By.ANDROID_UIAUTOMATOR, '.text("Sauce Labs Fleece Jacket")')
        self.lbl_price = (By.ANDROID_UIAUTOMATOR, '.text("$49.99")')
        self.btn_add_cart = (By.ACCESSIBILITY_ID, "Add To Cart button")
        self.lbl_cart = (By.ANDROID_UIAUTOMATOR, '.text("1")')
        self.btn_cart = (By.ACCESSIBILITY_ID, "cart badge")
        self.image_jacket = (By.XPATH, "//android.view.ViewGroup[@content-desc='product row']/android.widget.ImageView")
        self.lbl_detail_name = (By.ACCESSIBILITY_ID, "product label")
        self.lbl_detail_price = (By.ACCESSIBILITY_ID, "product price")
        self.image_color = (By.XPATH, "//android.view.ViewGroup[@content-desc='gray circle']/android.view.ViewGroup")
        self.lbl_checkout = (By.ANDROID_UIAUTOMATOR, '.text("Proceed To Checkout")')
