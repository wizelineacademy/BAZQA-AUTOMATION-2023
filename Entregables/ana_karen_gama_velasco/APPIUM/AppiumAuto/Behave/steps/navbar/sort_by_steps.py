from behave import *
from screens.navbar.sort_screens import SortScreen


@When('we select price asc option')
def step_impl(context):
    sort_screen = SortScreen(context)
    sort_screen.tap_element(*sort_screen.btn_price_asc)



