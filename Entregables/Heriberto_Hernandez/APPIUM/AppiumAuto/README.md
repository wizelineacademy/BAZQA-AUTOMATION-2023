
# Proyecto de Appium

Este proyecto  se desarrollo para  continuar con el Framework  construido desde cero para la automatizacion en la app de Saudemo con ayuda del lenguaje Python, esto nos ayudara a  reafirmar los temas vistos en clase referente a la Automatizacion en lenjuage Python.Incluye escenarios positivos  sugeridos en el Capstone Project.




# Estructura de proyecto

```
appium-python
     ├── Report                 # Contiene los reportes  de los casos ejecutados en la herramienta Allure
     ├── screens                # Contiene las clases de objetos de página necesarias para interactuar con la aplicación móvil 
     ├── steps                  # Contiene los pasos a ejecucarse en cada pantalla utiliazdos en los casos de prueba
     ├── utils                  # Contiene  los diccionarios necesarios y el archivo de acciones comunes.    
     ├── venv                   # contiene el archivo  de los datos de las pruebas README    
     ...
```


# Desarrollo de las pruebas


## Herramientas necesarias para la ejecucion 

* IDE: Pycharm
* Lenguaje: Python
* Emulador Android Studio
* Appium Server
* Allure 
* Windows PowerShell


## Preparación para la ejecucion de la prueba



1. Para la Ejecución del la prueba es necesario iniciar el Emulador Android Studio con el dispositivo virtual que utlizaremos.

2. Instalar en el dispositivo o emulador el APK de la version saucedemo.apk
3. Descargar el proyecto a ejecutar en la ubicacion antes mencionada
4. Ejecutar la herramienta Appium Server GUI  la cual nos servira de interfaz entre la APP y el proyecto a validar.

5.  Ejecutar la IDE: Pycharm y abrir el proyecto previmamente descargado

### Para la ejecución de pruebas es necesario la instalacion de los siguientes comando
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



6. Para la  la ejecucion de las prueba utilizaremos los archivos  de las feacture siguientes.

```

[data.product.screen.feature]
[home.screen.feature]
[my.cart.screen.feature]


```





que se encuentra en la carpeta 
```
    "feacture"
    
    pythonProject1\AppiumAuto\behave\feactures

```



## Ejecucion de la prueba

7.- Para la ejecucion de pruebas los siguientes comandos te podrian ayudas

````
    pytest                          # Ejecutar todas las pruebas
    pytest -m 'smoke'               # Ejecutar las pruebas de Humo
    pytest -m 'regression'          # ejecutar las pruebas de regresion
 
````

Los casos de prueba contemplan 1 prueba de Smoke y 2 pruebas de regresion


La terminal del IDE: Pycharm debe mostrarnos el resultado de la prueba exitosa
````
[data.product.screen.feature].- seleccion del primer prudcto y validacion de precio y nombre
[home.screen.feature].- Seleccionar la opcion de ordenamiento de procdutos  de menor a mayor
[my.cart.screen.feature].- Selecciona un producto lo ingresa al carrito y valida su precio y nombre

````


============================= test session starts =============================

3 features passed, 0 failed, 0 skipped
3 scenarios passed, 0 failed, 0 skipped
14 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m14.218s


