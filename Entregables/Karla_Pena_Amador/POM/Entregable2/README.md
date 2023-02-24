
# Prueba de login

Este proyecto contiene la automatización de casos de prueba del modulo de login.
Para eso es necesario considerar la instalación de las siguientes herramientas de software.

* Python3
* Appium server
* Appium inspector
* IDE Pycharm community considerando la instalación de paquetes.
    * Appium-Python-client
    * Pytest
    * Flake8
    * Allure

## Python3
Entrar a la página oficial https://www.python.org/ y descargar de acuerdo al tipo de sistema operativo con el que se va a trabajar.  

## Appium server
Ingresar a la página oficial https://appium.io/downloads.html seleccionar Appium Desktop Apps mismo que direccionará a github para que descargue el ejecutable que corresponda a su sistema operativo.


## Appium inspector
Para instalar appium inspector es necesario ingresar a la siguiente url https://github.com/appium/appium-inspector/releases mima que direcciona al repositorio que tiene los ejecutables de acuerdo a cada tipo de sistema operativo.


## IDE Pycharm Community
Ingresar a la página oficial https://www.jetbrains.com/es-es/pycharm/ y descargar el
ejecutable Community. Recuerde que durante la instalación se deben ambientar las variables de entorno.
El mismos ejecutable presenta una pantalla que permite la configuración de las variables de entorno. 

Una vez que se tenga el IDE, instalar los siguientes paquetes con el uso de la terminal.  
Nota: es importante antes instalar nodeJS para ejecutar los comandos con el prefijo npm. 

Considerar los siguientes requerimientos para correr el programa [requirements.txt](requirements.txt)

Se agregan los comandos de los paquetes principales.

    Appium-python-client con el comando

        pip install Appium-Python-Client
    
    Pytest con el comando

        pip install -U pytest

    Flake8 con el comando

        npm install flake8
    
    Allure reports

        npm install -g allure-commandline --save-dev

  

## Set de pruebas
Considerar que se debe generar un archivo `.env` en la carpeta utils y contener las variables de las credenciales a ingresar, mismas que se deben solicitar a negicio.
```bash
USERNAME_CAP=" "
PASSWORD_CAP=" "
```
Para correr el set de pruebas de regresión son con  los siguientes comandos.  


```bash
Pruebas de humo

  pytest -v -m smoketests

Pruebas de regresión

  pytest -v -m regression

```

Para generar reporte con Allure ejecutar los siguientes comandos.
```bash
  pytest --alluredir=allure-report/

  allure serve ./allure-report  
```
