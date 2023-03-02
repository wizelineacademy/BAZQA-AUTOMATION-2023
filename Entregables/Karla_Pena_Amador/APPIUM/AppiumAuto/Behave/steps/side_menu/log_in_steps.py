from behave import *
from screens.side_menu.log_in_screen import LoginScreen
from utils.dictionaries.log_in_text import LOGIN_TEXTS


# aunque en el feature este and en los pasos se agrega then
@Then('we enter the correct user')
def step_impl(context):
    log_in = LoginScreen(context)
    # log_in.fill_text(*log_in.txt_username, text=LOGIN_TEXTS.get('txt_username'))
    log_in.fill_text(*log_in.txt_username, text=context.STANDARD_USER)


@Then('we enter the correct password')
def step_impl(context):
    log_in = LoginScreen(context)
    # log_in.fill_text(*log_in.txt_password, text=LOGIN_TEXTS.get('txt_password'))
    log_in.fill_text(*log_in.txt_password, text=context.PASSWORD)


@Then('we tap button Login')
def step_impl(context):
    log_in = LoginScreen(context)
    log_in.tap_element(*log_in.btn_login)

