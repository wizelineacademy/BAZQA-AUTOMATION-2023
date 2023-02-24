import os
import pytest
from screens.HomeScreen import HomeScreen
from screens.LoginScreen import LoginScreen


@pytest.mark.smoke
@pytest.mark.regression
def test_exitoso(driver):
    username = os.getenv("correo@correo.com")
    password = os.getenv("contraseña")
    home_screen = HomeScreen(driver)
    home_screen.go_to_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert home_screen.elemento_es_mostrado(*home_screen.lbl_products)


@pytest.mark.regression
def test_user_incorrecto(driver):
    username = os.getenv("correoincorrecto@correo.com")
    password = os.getenv("contraseña")
    home_screen = HomeScreen(driver)
    home_screen.go_to_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert login_screen.elemento_es_mostrado(*login_screen.lbl_error)


@pytest.mark.regression
def test_user_blocked(driver):
    username = "usuariobloqueado@correo.com"
    password = "contraseña"
    home_screen = HomeScreen(driver)
    home_screen.go_to_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert login_screen.elemento_es_mostrado(*login_screen.lbl_error)


@pytest.mark.smoke
@pytest.mark.regression
def test_empty_user(driver):
    username = ""
    password = "correoincorrecto@correo.com"
    home_screen = HomeScreen(driver)
    home_screen.go_to_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert login_screen.elemento_es_mostrado(*login_screen.lbl_msj_error)
