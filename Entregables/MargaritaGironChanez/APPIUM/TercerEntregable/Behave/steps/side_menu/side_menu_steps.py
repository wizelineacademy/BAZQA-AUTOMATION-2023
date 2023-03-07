from screens.side_menu.side_menu_screen import SideMenuScreen
from behave import *


@Then('we tap on Log in')
def step_impl(context):
    side_menu = SideMenuScreen(context)
    side_menu.tap_element(*side_menu.btn_login)
