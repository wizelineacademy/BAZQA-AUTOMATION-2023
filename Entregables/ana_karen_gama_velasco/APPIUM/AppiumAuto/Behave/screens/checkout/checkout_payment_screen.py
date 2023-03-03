from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class CheckOutPaymentScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.txt_full_name = (By.ACCESSIBILITY_ID, "Full Name* input field")
        self.txt_card_number = (By.ACCESSIBILITY_ID,
                                "Card Number* "
                                "input field")
        self.txt_expiration_date = (By.ACCESSIBILITY_ID,
                                    "Expiration Date*"
                                    " input field")
        self.txt_security_code = (By.ACCESSIBILITY_ID,
                                  "Security Code* "
                                  "input field")
        self.btn_review_order = (By.ACCESSIBILITY_ID,
                                 "Review Order button")
