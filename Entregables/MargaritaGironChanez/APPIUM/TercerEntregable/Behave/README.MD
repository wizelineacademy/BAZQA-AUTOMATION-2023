Tercer entregable 
A continuación enlisto las configuraciones, comandos para ejecutar el proyecto correctamente
1.Instalar los paquetes incluidos en el archivo requirements.txt
   pip install -r requirements.txt

2.En el archivo environment.py --> desired_caps_setup --> colocar la plataforma, el sistema operativo, el nombre del dispositivo y la ruta donde se encuentra el apk

3.En el archivo .example_env se encuentran los ejemplos de como definir las credenciales

4.Suite de regresión
  @Regression

6.Análisis de código estático con Flake8
   flake8 ./features
   flake8 ./screens
   flake8 ./steps
