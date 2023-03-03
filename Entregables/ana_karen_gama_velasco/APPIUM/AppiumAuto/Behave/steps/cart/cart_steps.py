from behave import *
from screens.cart.cart_screen import CartScreen


@Then('we validate products name "{name_product}"')
def step_impl(context, name_product):
    cart_screen = CartScreen(context)
    cart_screen.assert_text(*cart_screen.lbl_name_product, text=name_product)


@Then('we validate products price "{price_product}"')
def step_impl(context, price_product):
    cart_screen = CartScreen(context)
    cart_screen.assert_text(*cart_screen.lbl_price_product, text=price_product)


@When('we tap on proceed to checkout')
def step_impl(context):
    cart_screen = CartScreen(context)
    cart_screen.tap_element(*cart_screen.btn_check_out)
