import pytest

from screens.HomeScreen import HomeScreen
from screens.LoginScreen import LoginScreen
from dotenv import load_dotenv
import os

class TestLogin:

    load_dotenv("./utils/.env")


    @pytest.mark.regression
    def test_exitoso(self, driver):
        username = os.getenv("USERNAME_CAP")
        password = os.getenv("PASSWORD_CAP")
        home_screen = HomeScreen(driver)
        home_screen.go_to_login()
        login_screen = LoginScreen(driver)
        login_screen.login(username, password)
        assert home_screen.elemento_es_mostrado(*home_screen.lbl_products)


    @pytest.mark.regression
    def test_usuario_incorrecto(self, driver):
        username = "hola"
        password = os.getenv("PASSWORD_CAP")
        home_screen = HomeScreen(driver)
        home_screen.go_to_login()
        login_screen = LoginScreen(driver)
        login_screen.login(username, password)
        assert home_screen.elemento_es_mostrado(*login_screen.lbl_credentials)


    @pytest.mark.smoketest
    def test_contraseña_incorrecta(self, driver):
        username = os.getenv("USERNAME_CAP")
        password = "prueba"
        home_screen = HomeScreen(driver)
        home_screen.go_to_login()
        login_screen = LoginScreen(driver)
        login_screen.login(username, password)
        assert home_screen.elemento_es_mostrado(*login_screen.lbl_credentials)


    @pytest.mark.smoketest
    def test_campo_vacio(self, driver):
        username = ""
        password = os.getenv("PASSWORD_CAP")
        home_screen = HomeScreen(driver)
        home_screen.go_to_login()
        login_screen = LoginScreen(driver)
        login_screen.login(username, password)
        assert home_screen.elemento_es_mostrado(*login_screen.lbl_user_required)
