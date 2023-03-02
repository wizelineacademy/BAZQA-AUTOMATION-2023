import pytest
from screens.LoginPage import LoginPage
from tests.fixtures import driver, constants


class TestLoginSwagLabs:

    @pytest.mark.smoke
    def test_login_valido(self, driver, constants):
        login_page = LoginPage(driver)
        login_page.Login(constants.USUARIOS['ESTANDAR']['USUARIO'], constants.USUARIOS['ESTANDAR']['CONTRASENA'])
        message_assert = login_page.is_login_successful()
        assert message_assert == constants.TEXTOS['TITULO_PRODUCTOS']

    @pytest.mark.regression
    def test_login_sin_usuario(self, driver, constants):
        login_page = LoginPage(driver)
        login_page.Login("", constants.USUARIOS['ESTANDAR']['CONTRASENA'])
        message_assert = login_page.is_login_successful()
        assert message_assert == constants.MENSAJES['ERROR_MENSAJE']['SIN_USUARIO']

    @pytest.mark.regression
    def test_login_sin_contrasena(self, driver, constants):
        login_page = LoginPage(driver)
        login_page.Login(constants.USUARIOS['ESTANDAR']['USUARIO'], "")
        message_assert = login_page.is_login_successful()
        assert message_assert == constants.MENSAJES['ERROR_MENSAJE']['SIN_CONTRASEÑA']

    @pytest.mark.regression
    def test_login_usuario_incorrecto(self, driver, constants):
        login_page = LoginPage(driver)
        login_page.Login(constants.USUARIOS['USUARIO_CONTRASENA_INCORRECTO']['USUARIO'], constants.USUARIOS['USUARIO_CONTRASENA_INCORRECTO']['CONTRASENA'])
        message_assert = login_page.is_login_successful()
        assert message_assert == constants.MENSAJES['ERROR_MENSAJE']['USUARIOS_INVALIDOS']
