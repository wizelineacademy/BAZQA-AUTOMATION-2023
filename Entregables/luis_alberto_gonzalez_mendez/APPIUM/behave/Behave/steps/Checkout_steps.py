from behave import *
from screens.Login_screen import LoginScreen
from screens.Checkout_screen import Checkout
from utils.dictionaries.checkout_text import FORM, PAGE_TEXTS

@Given('the user has added multiple items to the shopping cart')
def step_impl(context):
    checkout = Checkout(context)
    checkout.find_and_click_element(*checkout.add_product2)
    checkout.find_and_click_element(*checkout.add_product1)


@When('the user selects the cart option')
def step_impl(context):
    checkout = Checkout(context)
    checkout.find_and_click_element(*checkout.tap_cart)

@When('the purchase confirmation screen is displayed')
def step_impl(context):
    checkout = Checkout(context)
    checkout.scroll(*checkout.button_checkout)


@When('customer data is entered')
def step_impl(context):
    checkout = Checkout(context)
    checkout.enter_text(*checkout.form_name, text=FORM.get("NAME"))
    checkout.enter_text(*checkout.form_last_name, text=FORM.get("LAST_NAME"))
    checkout.enter_text(*checkout.form_postal_code, text=FORM.get("POSTAL_CODE"))


@When('I tap the continue button')
def step_impl(context):
    checkout = Checkout(context)
    checkout.find_and_click_element(*checkout.button_continue)


@When('we scroll to find the button')
def test_scroll(context):
    checkout = Checkout(context)
    checkout.scroll(*checkout.button_terminar)


@Then('you should be redirected to the order processed screen')
def test_scroll(context):
    checkout = Checkout(context)
    checkout.assert_text(*checkout.checkout_page, text=PAGE_TEXTS.get("FINAL_PAGE"))
