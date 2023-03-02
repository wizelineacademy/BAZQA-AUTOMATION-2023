
# Proyecto POM en Python

Este proyecto  se desarrollo para contruir un Framework desde cero para la automatizacion en la app de Saudemo con ayuda del lenguaje Python, esto nos ayudara a  reafirmar los temas vistos en clase referente a la Automatizacion en lenjuage Python.Incluye escenarios positivos y  3 negativos. 


# Estructura de proyecto

```
appium-python
     ├── Report                 # Contiene los reportes  de los casos ejecutados en la herramienta Allure
     ├── screens                # Contiene las clases de objetos de página necesarias para interactuar con la aplicación móvil 
     ├── tests                  # Contiene los archivos de los casos de prueba para ejecutarse
     ├── venv                   # contiene el archivo  de los datos de las pruebas README    
     ...
```


## Pruebas en aplicación saucedemo

Herramientas necesarias para la ejecucion 

* IDE: Pycharm
* Lenguaje: Python
* Emulador Android Studio
* Appium Server
* Allure 
* Windows PowerShell


## Preparación para la ejecucion de la prueba



1. Para la Ejecucion del la prueba es necesario iniciar el Emulador Android Studio con el dispositivo virtual que utlizaremos

2. Instalar en el dispositivo el APK de la version saucedemo.apk
3. Descargar el proyecto a ejecutar en la ubicacion antes mencionada
4. Ejecutar la herramienta Appium Server GUI  la cual nos servira de interfaz entre la APP y el proyecto

5. Ejecutar la IDE: Pycharm y abrir el proyecto previmamente descargado

### Para la ejecucion de pruebas es necesario la instalacion de los siguientes comando
```
# Command to install PyTest library
pip install pytest

# Command to install Appium library
pip install Appium-Python-Client

# Command to install Flake8 library
pip install flake8

# Command to install Allure library
pip install allure-pytest

# Command to install allure application (MacOS)
brew install allure
```



6. Para la  la ejecucion de las prueba utilizaremos el archivo

```
test_login.py

```
que se encuentra en la siguiente ubicacion:
```
\DialerAutomationTest\DialerAutomationTest\tests

```


7. Para la ejecucion de pruebas ss necesario la creacion un archivo de entorno `.env` dentro de la carpeta raíz, esta nos ayudara a  para iniciar sesión en la aplicación con sus propias credenciales durante la ejecución de la prueba y evitar errores durante el rendimiento.
El archivo de entorno tiene que contener las siguientes variables y valores de acuerdo a sus credenciales:
```
USERNAMEP=bob@example.com
WIZEPASS=10203040
```
## Ejecucion de la prueba

8. Para la ejecucion de pruebas los siguientes comandos te podrian ayudas

````
    pytest                          # Ejecutar todas las pruebas
    pytest -m 'smoke'               # Ejecutar las pruebas de Humo
    pytest -m 'regression'          # ejecutar las pruebas de regresion
 
````

Los casos de prueba contemplan 1 exitoso y 3 casos erroneos, ademas de las pruebas de Humo y regresion

````

  test_login.py::test_exitoso 
test_login.py::test_erroneo 
test_login.py::test_sin_datos 
test_login.py::test_sin_pass 
````


La terminal del IDE: Pycharm debe mostrarnos el resultado de la prueba exitosa


  pytest -m test_login.py   

============================= test session starts =============================
collecting ... collected 6 items / 2 deselected / 4 selected

test_login.py::test_exitoso 
test_login.py::test_erroneo 
test_login.py::test_sin_datos 
test_login.py::test_sin_pass 



## Generacion del reporte en allure

Para este reporte  utilizaremos la herramienta windows PowerShell
```bash
 E:\DialerAutomationTest\DialerAutomationTest\reports

```
