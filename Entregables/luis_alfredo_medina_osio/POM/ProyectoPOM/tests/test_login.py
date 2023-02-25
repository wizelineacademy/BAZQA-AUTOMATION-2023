
from dotenv import load_dotenv
from ProyectoPOM.screens.HomeScreen import HomeScreen
from ProyectoPOM.screens.LoginScreen import LoginScreen
import os
import pytest

load_dotenv(".\\ProyectoPOM\\.env")

@pytest.mark.smoketest
def test_exitoso(driver):
    username = os.getenv("USERNAMEOK")
    password = os.getenv("CONTRAOK")
    home_screen = HomeScreen(driver)
    home_screen.go_to_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert home_screen.elemento_es_mostrado(*home_screen.lbl_products)

@pytest.mark.smoketest
def test_user_error(driver):
    username = os.getenv("USERFAKE")
    password = os.getenv("CONTRAOK")
    home_screen = HomeScreen(driver)
    home_screen.go_to_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert login_screen.elemento_es_mostrado(*login_screen.lbl_userfake)

@pytest.mark.smoketest
def test_pass_error(driver):
    username = os.getenv("USERNAMEOK")
    password = os.getenv("CONTRAFAKE")
    home_screen = HomeScreen(driver)
    home_screen.go_to_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert login_screen.elemento_es_mostrado(*login_screen.lbl_passfake)

@pytest.mark.regresion
def test_locked_user(driver):
    username = os.getenv("USERNAMELOCKED")
    password = os.getenv("CONTRAOK")
    home_screen = HomeScreen(driver)
    home_screen.go_to_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert login_screen.elemento_es_mostrado(*login_screen.lbl_userlocked)
