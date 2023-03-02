import pytest
from DialerAutomationTest.tests.conftest import data
from DialerAutomationTest.screens.LoginScreen import LoginScreen
from DialerAutomationTest.screens.HomeScreen import HomeScreen


# caso exitoso de inicio de sesion
@pytest.mark.smoke
def test_login_exitoso(driver, data):
    home_screen = HomeScreen(driver)
    home_screen.go_to_login()
    login_screen = LoginScreen(driver)
    login_screen.login(data["USERNAMEP"], data["WIZEPASS"])
    assert home_screen.elemento_es_mostrado(*home_screen.lbl_products)


# Caso de prueba erroneo, usuario incorrecto en el flujo del login
@pytest.mark.regression
def test_usuario_contrasena_incorrectos(driver):
    username = "username"
    password = "prueba"

    home_screen = HomeScreen(driver)
    home_screen.go_to_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert login_screen.elemento_es_mostrado(*login_screen.lbl_erroneos)

# caso de prueba erroneo, login  sin usuario
@pytest.mark.regression
def test_usuario_contrasena_sin_datos(driver):
    home_screen = HomeScreen(driver)
    home_screen.go_to_login()
    login_screen = LoginScreen(driver)
    login_screen.login("", "")
    assert login_screen.elemento_es_mostrado(*login_screen.lbl_sin_username)

# caso de prueba erroneo,  login  sin password
@pytest.mark.regression
def test_sin_contrasena(driver, data):
    home_screen = HomeScreen(driver)
    home_screen.go_to_login()
    login_screen = LoginScreen(driver)
    login_screen.login(data["USERNAMEP"], "")
    assert login_screen.elemento_es_mostrado(*login_screen.lbl_sin_password)
