from behave import *
from screens.detail_product.checkout_address_screen import CheckoutAddressScreen
from utils.dictionaries.checkout_texts import CHECKOUT_TEXTS


@When('we enter the fullname')
def step_impl(context):
    check_out = CheckoutAddressScreen(context)
    check_out.fill_text(*check_out.txt_name, text=CHECKOUT_TEXTS.get('txt_name'))


@When('we enter the address')
def step_impl(context):
    check_out = CheckoutAddressScreen(context)
    check_out.fill_text(*check_out.txt_address, text=CHECKOUT_TEXTS.get('txt_address'))


@When('we enter the city')
def step_impl(context):
    check_out = CheckoutAddressScreen(context)
    check_out.fill_text(*check_out.txt_city, text=CHECKOUT_TEXTS.get('txt_city'))


@When('we enter the state')
def step_impl(context):
    check_out = CheckoutAddressScreen(context)
    check_out.fill_text(*check_out.txt_state, text=CHECKOUT_TEXTS.get('txt_state'))


@When('we enter the zipcode')
def step_impl(context):
    check_out = CheckoutAddressScreen(context)
    check_out.fill_text(*check_out.txt_zipcode, text=CHECKOUT_TEXTS.get('txt_zipcode'))


@When('we enter the country')
def step_impl(context):
    check_out = CheckoutAddressScreen(context)
    check_out.fill_text(*check_out.txt_country, text=CHECKOUT_TEXTS.get('txt_country'))


@When('we tap payment button')
def step_impl(context):
    check_out = CheckoutAddressScreen(context)
    check_out.tap_element(*check_out.btn_to_payment)
