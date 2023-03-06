from behave import *
from screens.home_screen import HomeScreen
from utils.dictionaries.home_screen_texts import HOME_TEXTS


@Step('we are in the Home Page')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.find_element(*home_screen.lbl_products)


@Then('we see the Products label')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.assert_text(*home_screen.lbl_products, text=HOME_TEXTS.get('lbl_products'))


@Given('we tap sort button')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.btn_sort)


@Given('we tap on the side menu')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.menu_side)
