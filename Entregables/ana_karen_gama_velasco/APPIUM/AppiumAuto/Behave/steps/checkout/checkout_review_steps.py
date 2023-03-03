from behave import *
from screens.checkout.checkout_review_screen import CheckoutReview


@When('we tap on place order')
def step_impl(context):
    chout_screen = CheckoutReview(context)
    chout_screen.tap_element(*chout_screen.btn_place_order)
