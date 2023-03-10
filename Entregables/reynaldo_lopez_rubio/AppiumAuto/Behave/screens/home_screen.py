from appium.webdriver.common.appiumby import AppiumBy as By
from Utils.common_actions import CommondActions


class HomeScreen(CommondActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.lbl_products = (By.ANDROID_UIAUTOMATOR, '.text("Products")')
        self.menu_side = (By.ACCESSIBILITY_ID, "open menu")
        self.img_bike = (By.XPATH, "(//android.view.ViewGroup[@content-desc="
                                   "'store item'])"
                                   "[2]/android.view.ViewGroup["
                                   "1]/android.widget.ImageView")
        self.lbl_Bike = (By.ANDROID_UIAUTOMATOR, '.text("Sauce Labs '
                                                 'Bike Light")')
        self.lbl_Precio = (By.ACCESSIBILITY_ID, "product price")
        self.btn_ordenar = (By.ACCESSIBILITY_ID, "sort button")
        self.btn_MayoraMenor = (By.ACCESSIBILITY_ID, "priceAsc")
