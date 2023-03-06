from behave import *
from Utils.dictionaries.home_screen_text import HOME_TEXTS
from screens.side_menu.log_in_screen import LogInScreen


@Then("we enter the correct user")
def step_impl(context):
    log_in = LogInScreen(context)
    log_in.fill_text(*log_in.txt_username, text=context.STANDARD_USER)

@Then("we enter the correct password")
def step_impl(context):
    log_in = LogInScreen(context)
    log_in.fill_text(*log_in.txt_password, text=context.PASSWORD)


@Then('Tap on the Log In button')
def step_impl(context):
    log_in = LogInScreen(context)
    log_in.tap_element(*log_in.btn_login)
