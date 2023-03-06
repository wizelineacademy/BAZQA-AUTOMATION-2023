from behave import *
from screens.detail_product.sort_screen import SortProductScreen
from utils.dictionaries.sort_texts import SORT_PRODUCT


@Then('we tap price-ascending')
def step_impl(context):
    sort_menu = SortProductScreen(context)
    sort_menu.tap_element(*sort_menu.btn_price_asc)

