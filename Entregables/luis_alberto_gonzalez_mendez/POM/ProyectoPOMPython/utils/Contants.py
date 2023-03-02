from dotenv import dotenv_values

class Constants:
    data = dotenv_values("../.env")

    def __init__(self):
        self.MENSAJES = {
            "ERROR_MENSAJE": {
               "SIN_USUARIO": "Usuario es requerido",
               "SIN_CONTRASEÑA": "Contraseña es requerida",
               "USUARIOS_INVALIDOS": "El usuario y contraseña no coinciden con ningun usuario en este servicio."
               }
           }

        self.USUARIOS = {
             "ESTANDAR":{
             "USUARIO": self.data['USERNAME'],
             "CONTRASENA": self.data['PASSWORD']
            },
            "USUARIO_CONTRASENA_INCORRECTO": {
            "USUARIO": "RT5$",
            "CONTRASENA": "#rgrhty"
            }
        }

        self.TEXTOS = {
            "TITULO_PRODUCTOS": "PRODUCTOS"
         }