import secrets
import string

from screens.screenLogin import screenLogin
from screens.screenMenu import screenMenu
from screens.screenProduct import screenProduct


def base_login(driver, username, password):
    product = screenProduct(driver)
    product.abrirMenu()
    menu = screenMenu(driver)
    menu.opcionLogin()
    login = screenLogin(driver)
    login.login(username, password)


def generacion_aleatoria_password():
    letras = string.ascii_letters
    digitos = string.digits
    caracteres_especiales = string.punctuation
    alfabeto = letras + digitos + caracteres_especiales
    password_longitud = 12
    password = ''
    for i in range(password_longitud):
        password += ''.join(secrets.choice(alfabeto))
    return password
