
from behave import *
from screens.data_product_screen.data_product_screen import DataProductScreen
from utils.dictionaries.data_screen_text import DATA_TEXTS



@Step('we tap on add car')
def step_impl(context):
    data_product_screen = DataProductScreen(context)
    data_product_screen.tap_element(*data_product_screen.btn_add)


@Step('we see the Name Product')
def step_impl(context):
    data_product_screen = DataProductScreen(context)
    data_product_screen.assert_text(*data_product_screen.lbl_name, text=DATA_TEXTS.get("lbl_name_product"))


@Step('we see the Price Product')
def step_impl(context):
    data_product_screen = DataProductScreen(context)
    data_product_screen.assert_text(*data_product_screen.lbl_price, text=DATA_TEXTS.get('lbl_price_product'))


@Then('we tap on cart badge')
def step_impl(context):
    data_product_screen = DataProductScreen(context)
    data_product_screen.tap_element(*data_product_screen.btn_cart)

@Step('we swap screen')
def step_impl(context):
    data_product_screen = DataProductScreen(context)
    data_product_screen.swap_screen()


