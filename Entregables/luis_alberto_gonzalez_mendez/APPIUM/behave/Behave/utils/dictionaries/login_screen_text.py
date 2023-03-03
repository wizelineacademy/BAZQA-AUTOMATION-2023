import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("USR")
password = os.getenv("PSW")

HOME_TEXTS = {
    'HOME_PAGE': "PRODUCTOS"
}

USUARIOS = {
             "USERNAME": username,
             "PASSWORD": password
        }