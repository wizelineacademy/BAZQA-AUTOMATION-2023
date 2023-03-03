import time
from behave import *
from screens.checkout.checkout_payment_screen import CheckOutPaymentScreen
from utils.dictionaries.checkout_screen_texts import *


@When('we enter the buyer full name')
def step_impl(context):
    time.sleep(2.4)
    chout_screen = CheckOutPaymentScreen(context)
    chout_screen.fill_text(*chout_screen.txt_full_name, text=FULL_NAME.get("FULL_NAME"))


@When('we enter the card number')
def step_impl(context):
    chout_screen = CheckOutPaymentScreen(context)
    chout_screen.fill_text(*chout_screen.txt_card_number, text=CARD.get("CARD"))


@When('we enter the expiration date')
def step_impl(context):
    chout_screen = CheckOutPaymentScreen(context)
    chout_screen.fill_text(*chout_screen.txt_expiration_date, text=CARD.get("EXP_DATE"))


@When('we enter the security code')
def step_impl(context):
    chout_screen = CheckOutPaymentScreen(context)
    chout_screen.fill_text(*chout_screen.txt_security_code, text=CARD.get("SEC_CODE"))


@When('we tap on review order')
def step_impl(context):
    chout_screen = CheckOutPaymentScreen(context)
    chout_screen.tap_element(*chout_screen.btn_review_order)



