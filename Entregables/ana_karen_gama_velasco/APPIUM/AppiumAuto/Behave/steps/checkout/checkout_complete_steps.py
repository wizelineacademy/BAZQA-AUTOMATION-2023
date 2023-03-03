from behave import *
from screens.checkout.checkout_complete_screen import CheckoutComplete


@Then('we see the checkout complete')
def step_impl(context):
    chout_screen = CheckoutComplete(context)
    chout_screen.assert_text(*chout_screen.lbl_checkout_complete, text="Checkout Complete")


@Then('we tap the Continue Shopping')
def step_impl(context):
    chout_screen = CheckoutComplete(context)
    chout_screen.tap_element(*chout_screen.btn_continue_shopping)
