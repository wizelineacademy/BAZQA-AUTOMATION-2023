 PROYECTO APPIUM

En éste proyecto se realiza la automatización de los Casos de Prueba de la aplicación Saucedemo usando el patron de diseño POM y estructura Gherkin.

## Software requerido:

Para ejecutar los casos se requiere la instalación de programas indicados en el archivo requirements.txt

```PowerShell
behave==1.2.6
Appium-Python-Client==2.8.1
python-dotenv~=0.19.2
selenium==3.141.0
allure-behave==2.21.0

```


## Ejecución de Tests

Para correr un test suite, ejecutar el siguiente comando

```PowerShell
  behave ./Behave/features
```


## Reportes

Para generar un reporte con allure ejecutar el siguiente comando

```PowerShell
  behave -f allure_behave.formatter:AllureFormatter -o reports/ Behave/features
```
Para visualizar el reporte con allure ejecutar el siguiente comando

```PowerShell
  allure serve reports/
```