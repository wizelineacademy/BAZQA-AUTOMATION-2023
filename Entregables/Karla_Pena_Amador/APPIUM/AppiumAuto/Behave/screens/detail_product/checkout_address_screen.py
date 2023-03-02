from appium.webdriver.common.appiumby import AppiumBy as By

from utils.common_actions import CommonActions


class CheckoutAddressScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.txt_name = (By.ACCESSIBILITY_ID, "Full Name* input field")
        self.txt_address = (By.ACCESSIBILITY_ID, "Address Line 1* input field")
        self.txt_city = (By.ACCESSIBILITY_ID, "City* input field")
        self.txt_state = (By.ACCESSIBILITY_ID, "State/Region input field")
        self.txt_zipcode = (By.ACCESSIBILITY_ID, "Zip Code* input field")
        self.txt_country = (By.ACCESSIBILITY_ID, "Country* input field")
        self.btn_to_payment = (By.ACCESSIBILITY_ID, "To Payment button")
