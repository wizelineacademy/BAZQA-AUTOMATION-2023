from screens.my_cart_screen import CartScreen
from screens.home_screen import HomeScreen
from behave import *
from utils.dictionaries.home_screen_texts import HOME_TEXTS
from utils.dictionaries.my_cart_texts import CART_TEXTS


@Given('we select a product')
def step_impl(context):
    select_product = CartScreen(context)
    select_product.tap_product(*select_product.lbl_product)


@When('we validate the name of the product')
def step_impl(context):
    name_product = CartScreen(context)
    name_product.find_element(*name_product.lbl_jacket)


@When('we validate the price of the product')
def step_impl(context):
    price_product = CartScreen(context)
    price_product.find_element(*price_product.lbl_price)


@When('we tap on Add to Cart')
def step_impl(context):
    add_product = CartScreen(context)
    add_product.tap_product(*add_product.btn_add_cart)


@Then('the cart badge shows an added product')
def step_impl(context):
    validate_cart = CartScreen(context)
    validate_cart.assert_text(*validate_cart.lbl_cart, text=CART_TEXTS.get('val_cart'))


@Given('we tap a product')
def step_impl(context):
    choose_product = CartScreen(context)
    choose_product.tap_product(*choose_product.lbl_product)


@Given('we Add to Cart')
def step_impl(context):
    add_products = CartScreen(context)
    add_products.tap_product(*add_products.btn_add_cart)


@Given('we tap my cart')
def step_impl(context):
    tap_cart = CartScreen(context)
    tap_cart.tap_product(*tap_cart.btn_cart)


@When('we validate the image')
def step_impl(context):
    validate_image = CartScreen(context)
    validate_image.find_element(*validate_image.image_jacket)


@When('we validate the name label')
def step_impl(context):
    name_label = CartScreen(context)
    name_label.find_element(*name_label.lbl_detail_name)


@When('we validate the price label')
def step_impl(context):
    price_label = CartScreen(context)
    price_label.find_element(*price_label.lbl_detail_name)


@When('we validate the color')
def step_impl(context):
    color_label = CartScreen(context)
    color_label.find_element(*color_label.image_color)


@Then('the button Proceed To Checkout is available')
def step_impl(context):
    checkout_button = CartScreen(context)
    checkout_button.assert_text(*checkout_button.lbl_checkout, text=CART_TEXTS.get('lbl_checkout'))



