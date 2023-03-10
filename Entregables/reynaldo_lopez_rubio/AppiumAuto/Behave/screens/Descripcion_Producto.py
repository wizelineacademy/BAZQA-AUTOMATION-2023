from appium.webdriver.common.appiumby import AppiumBy as By
from Utils.common_actions import CommondActions


class DescripcionProducto(CommondActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.btn_ADDCarrito = (
            By.ACCESSIBILITY_ID, "Add To Cart button")
        self.btn_carrito = (By.ACCESSIBILITY_ID, "cart badge")
        self.etiqueta_producto = (By.ACCESSIBILITY_ID, "product label")
        self.etiqueta_precio = (By.ANDROID_UIAUTOMATOR, '.text("$9.99")')
