import pytest
from dotenv import load_dotenv
from screens.HomeScreen import HomeScreen
from screens.LoginScreen import LoginScreen
import os

load_dotenv("E:\\Desarrollos\\Automatizacion_POM")


@pytest.mark.Regresion
@pytest.mark.SmokeTest
def test_exitoso(driver):
    username = os.getenv("USERNAMES")
    password = os.getenv("PASSWORDS")
    home_screen = HomeScreen(driver)
    home_screen.ir_a_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert home_screen.elemento_es_mostrado(*home_screen.lbl_products)


@pytest.mark.Regresion
def test_usuario_incorrecto(driver):
    username = "hola"
    password = os.getenv("PASSWORDS")
    home_screen = HomeScreen(driver)
    home_screen.ir_a_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert home_screen.elemento_es_mostrado(*home_screen.lbl_products)


@pytest.mark.Regresion
def test_Contrasena_incorrecto(driver):
    username = os.getenv("USERNAMES")
    password = "rttad"
    home_screen = HomeScreen(driver)
    home_screen.ir_a_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert home_screen.elemento_es_mostrado(*home_screen.lbl_products)


@pytest.mark.Regresion
def test_login_usuario_contrasena_incorrecta(driver):
    username = "ANDREA"
    password = "TORRES "
    home_screen = HomeScreen(driver)
    home_screen.ir_a_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert home_screen.elemento_es_mostrado(*home_screen.lbl_products)
