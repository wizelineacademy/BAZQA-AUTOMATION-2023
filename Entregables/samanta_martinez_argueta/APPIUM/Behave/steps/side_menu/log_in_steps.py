from behave import *
from screens.side_menu.log_in_screen import LogInScreen


@Then('we enter the correct user')
def step_impl(context):
    log_in = LogInScreen(context)
    log_in.fill_text(*log_in.txt_username, text=context.STANDARD_USER)


@Then('we enter the correct password')  # la etiqueta debe ser un Then aunque en el feature sea un And
def step_impl(context):
    log_in = LogInScreen(context)
    log_in.fill_text(*log_in.txt_password,
                     text=context.PASSWORD)  # se usa asterisco antes del método porque se está "pasando" todos los argumentos del método


@Then('we tap on the button login')
def step_impl(context):
    log_in = LogInScreen(context)
    log_in.tap_element(*log_in.btn_login)
