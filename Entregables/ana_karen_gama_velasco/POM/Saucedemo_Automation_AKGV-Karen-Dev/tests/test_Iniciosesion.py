import os
import pytest
from screens.screenProduct import screenProduct
from screens.screenLogin import screenLogin
from utils.actionsLibrary import generacion_aleatoria_password, base_login


class TestLogin:

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_login_exito(self, driver):
        username = os.getenv("USERNAMESUCCESS")
        password = os.getenv("PASSWORDSUCCESS")
        base_login(driver, username, password)
        product = screenProduct(driver)
        assert product.existe_el_elemento(*product.lbl_productos)

    @pytest.mark.regression
    def test_login_sin_username(self, driver):
        username = os.getenv("USERNAMENONEXISTENT")
        password = os.getenv("PASSWORDSUCCESS")
        base_login(driver, username, password)
        login = screenLogin(driver)
        assert login.existe_el_elemento(*login.lbl_dismatch)

    @pytest.mark.regression
    def test_login_no_username(self, driver):
        username = os.getenv("NODATA")
        password = os.getenv("PASSWORDSUCCESS")
        base_login(driver, username, password)
        login = screenLogin(driver)
        assert login.existe_el_elemento(*login.lbl_nousername)

    @pytest.mark.regression
    def test_login_no_password(self, driver):
        username = os.getenv("USERNAMESUCCESS")
        password = os.getenv("NODATA")
        base_login(driver, username, password)
        login = screenLogin(driver)
        assert login.existe_el_elemento(*login.lbl_nousername)

    @pytest.mark.regression
    def test_login_password_aleatorio(self, driver):
        username = os.getenv("USERNAMESUCCESS")
        password = generacion_aleatoria_password()
        base_login(driver, username, password)
        login = screenLogin(driver)
        assert login.existe_el_elemento(*login.lbl_dismatch)

    @pytest.mark.regression
    def test_login_user_name_con_emojis(self, driver):
        username = os.getenv("USERNAMEWITHEMOJI")
        password = os.getenv("PASSWORDSUCCESS")
        base_login(driver, username, password)
        login = screenLogin(driver)
        assert login.existe_el_elemento(*login.lbl_dismatch)
