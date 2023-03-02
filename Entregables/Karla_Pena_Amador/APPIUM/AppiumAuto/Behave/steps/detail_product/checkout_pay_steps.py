from behave import *
from screens.detail_product.checkout_pay_screen import CheckoutPayScreen
from utils.dictionaries.checkout_methodpay_texts import CHECKOUT_METHODPAY_TEXTS


@When('we enter the fullname to pay')
def step_impl(context):
    check_out_pay = CheckoutPayScreen(context)
    check_out_pay.fill_text(*check_out_pay.txt_name_pay, text=CHECKOUT_METHODPAY_TEXTS.get('txt_name_pay'))


@When('we enter the card number')
def step_impl(context):
    check_out_pay = CheckoutPayScreen(context)
    check_out_pay.fill_text(*check_out_pay.txt_card_number, text=CHECKOUT_METHODPAY_TEXTS.get('txt_card_number'))


@When('we enter the expiration date')
def step_impl(context):
    check_out_pay = CheckoutPayScreen(context)
    check_out_pay.fill_text(*check_out_pay.txt_expiration_date, text=CHECKOUT_METHODPAY_TEXTS.get('txt_expiration_date'))


@When('we enter the security code')
def step_impl(context):
    check_out_pay = CheckoutPayScreen(context)
    check_out_pay.fill_text(*check_out_pay.txt_security_code, text=CHECKOUT_METHODPAY_TEXTS.get('txt_security_code'))


@When('we tap review button')
def step_impl(context):
    check_out_pay = CheckoutPayScreen(context)
    check_out_pay.tap_element(*check_out_pay.btn_review_order)
