from behave import *
from screens.home_screen.sort_by_screen import SortBy


@Then('we tap on the Price Ascending')
def step_impl(context):
    sort_by_screen= SortBy(context)
    sort_by_screen.tap_element(*sort_by_screen.btn_priceAsc)


