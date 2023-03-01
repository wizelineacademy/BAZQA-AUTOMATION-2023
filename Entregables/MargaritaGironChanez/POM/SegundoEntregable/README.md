Segundo entregable 
A continuación enlisto las configuraciones, comandos para ejecutar el proyecto correctamente
1.Instalar los paquetes incluidos en el archivo requirements.txt
   pip install -r requirements.txt

2.En el archivo conftest --> DESIRED_CAPABILITIES --> appium:app poner la ruta en donde se encuentre alojado el apk

3.En el archivo pytest.ini.example se encuentran los ejemplos de como definir las credenciales

4.Ejecutar suite de regresión:
   pytest -v -m regression

5.Ejecutar suite para pruebas de humo
   pytest -v -m smoke

6.Análisis de código estático con Flake8
   flake8 ./screens
   flake8 ./tests

7.Después de ejecutar la suite regression/smoke, ejecutar el siguiente comando para generar el reporte
  allure serve ./reports
