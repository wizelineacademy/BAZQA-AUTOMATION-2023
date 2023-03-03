from behave import *
from screens.shop_cart_screen import ShoppingCart
from utils.dictionaries.shopping_cart_texts import CART_TEXTS
from appium.webdriver.common.touch_action import TouchAction


@When('we tap on Cart')
def step_impl(context):
    shopping_cart = ShoppingCart(context)
    shopping_cart.tap_element(*shopping_cart.btn_cart)


@Step('we see the Shopping Cart')
def step_impl(context):
    shopping_cart = ShoppingCart(context)
    shopping_cart.find_element(*shopping_cart.lbl_my_cart)
    shopping_cart.assert_text(*shopping_cart.lbl_my_cart, text=CART_TEXTS.get('lbl_my_cart'))


@Then('we validate the Product Name Added')
def step_impl(context):
    shopping_cart = ShoppingCart(context)
    shopping_cart.find_element(*shopping_cart.lbl_name_bolt)
    shopping_cart.assert_text(*shopping_cart.lbl_name_bolt, text=CART_TEXTS.get('lbl_name_bolt'))


@Then('we validate the Product Price Added')
def step_impl(context):
    shopping_cart = ShoppingCart(context)
    shopping_cart.find_element(*shopping_cart.lbl_price_bolt)
    shopping_cart.assert_text(*shopping_cart.lbl_price_bolt, text=CART_TEXTS.get('lbl_price_bolt'))
