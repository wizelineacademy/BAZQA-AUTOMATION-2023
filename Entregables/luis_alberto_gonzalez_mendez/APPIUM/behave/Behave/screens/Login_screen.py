from appium.webdriver.common.appiumby import AppiumBy
from utils.common_actions import CommonActions


class LoginScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)

        self.login_screen = (AppiumBy.XPATH,
                             '//android.widget.ScrollView[@content-desc="test-Login"]/android.view.ViewGroup/android.widget.ImageView[1]')
        self.username_input = (AppiumBy.ACCESSIBILITY_ID, 'test-Usuario')
        self.password_input = (AppiumBy.ACCESSIBILITY_ID, 'test-Contraseña')
        self.login_button = (AppiumBy.ACCESSIBILITY_ID, 'test-LOGIN')
        self.home_page = (AppiumBy.XPATH,
                          '//android.view.ViewGroup[@content-desc="test-Zona de caída del carrito de compras"]/android.view.ViewGroup/android.widget.TextView')
