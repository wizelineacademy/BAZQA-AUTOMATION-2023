from behave import Given
from behave import Then
from behave import When
from screens.home_screen import HomeScreen
from Utils.dictionaries.home_screen_text import HOME_TEXTS


@Given('we are in the Home Page')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.find_element(*home_screen.lbl_products)


@Then('we see the products label')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.assert_text(*home_screen.lbl_products,
                            text=HOME_TEXTS.get('lbl_products'))


@Given('we tap on the side menu')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.menu_side)


@Given('Dar Tap en el articulo')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.img_bike)


@Then('Validamos precio y nombre articulo')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.assert_text(*home_screen.lbl_Bike,
                            text=HOME_TEXTS.get('lbl_bike'))
    home_screen.assert_text(*home_screen.lbl_Precio,
                            text=HOME_TEXTS.get('lbl_precio'))


@Given('We tap on the order button')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.btn_ordenar)


@When('Tocamos el boton para ordenar el precio de Mayor a menor')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.btn_MayoraMenor)
