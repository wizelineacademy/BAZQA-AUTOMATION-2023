from cgitb import text

from behave import *
from screens.home_screen import HomeScreen
from utils.dictionaries.home_screen_texts import HOME_TEXTS
from utils.common_actions import CommonActions


@Step('we are in the Home Page')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.find_element(*home_screen.lbl_products)


@When('we tap on the filter')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.sort_button)
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.asc_button)


@Then('we see the products order by price')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.assert_test(*home_screen.first_element, text=HOME_TEXTS.get('first_element'))


@Given('we tap on the side menu')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.menu_side)
