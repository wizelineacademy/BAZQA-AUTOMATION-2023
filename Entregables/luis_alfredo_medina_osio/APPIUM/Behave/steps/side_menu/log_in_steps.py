from screens.side_menu.log_in_screen import LogInScreen
from screens.home_screen import HomeScreen
from behave import *
from utils.dictionaries.home_screen_texts import HOME_TEXTS


@When('we enter the correct user')
def step_impl(context):
    log_in = LogInScreen(context)
    log_in.fill_text(*log_in.txt_username, text=context.STANDARD_USER)


@When('we enter the correct password')
def step_impl(context):
    log_in = LogInScreen(context)
    log_in.fill_text(*log_in.txt_password, text=context.PASSWORD)


@When('we tap on Login button')
def step_impl(context):
    log_in = LogInScreen(context)
    log_in.tap_element(*log_in.btn_login)

