from behave import *
from screens.my_cart_screen.my_cart_screen import MyCart
from utils.dictionaries.my_cart_screen_text import MYCART_TEXTS


@Step('we see the Name Product1')
def step_impl(context):
    my_cart_screen = MyCart(context)
    my_cart_screen.assert_text(*my_cart_screen.lbl_name1, text=MYCART_TEXTS.get("lbl_name_product"))


@Step('we see the Price Product1')
def step_impl(context):
    my_cart_screen = MyCart(context)
    my_cart_screen.assert_text(*my_cart_screen.lbl_price1, text=MYCART_TEXTS.get("lbl_price_product"))