from behave import *
from screens.products.product_screen import ProductScreen
from utils.dictionaries.product_screen_texts import PRODUCT_TEXT


@Then('we see the Products price "{price}"')
def step_impl(context, price):
    product_screen = ProductScreen(context)
    product_screen.assert_text(*product_screen.lbl_price_product, text=price)


@Then('we see the Products name "{name}"')
def step_impl(context, name):
    product_screen = ProductScreen(context)
    product_screen.assert_text(*product_screen.lbl_name_product, text=name)


@When("we tap on the Cart")
def step_impl(context):
    product_screen = ProductScreen(context)
    product_screen.tap_element(*product_screen.btn_cart)


@When("we tap on Add To Cart")
def step_impl(context):
    product_screen = ProductScreen(context)
    product_screen.tap_element(*product_screen.btn_add_cart)


@When("we see a number one on the Cart")
def step_impl(context):
    product_screen = ProductScreen(context)
    product_screen.assert_text(*product_screen.lbl_number_cart, text=PRODUCT_TEXT.get('lbl_number_cart'))



