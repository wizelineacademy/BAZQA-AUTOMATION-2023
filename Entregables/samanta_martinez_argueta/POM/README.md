
# Automatización de login de la aplicación móvil "Sauce"

El proyecto contiene una suite de pruebas automatizada del login de la aplicación Sauce.





## Ejecución de pruebas

Antes de ejecutar una suite de pruebas o prueba individual, es necesario ingresar manualmente las credenciales del login ne el archivo ".env".

Si se requiere ejecutar las pruebas de humo, se debe ejecutar en la consola el siguiente comando:
```bash
  pytest -v -m smoketests
```

Si se requiere ejecutar las pruenas de regresión, se debe ejecutar en la consola el siguiente comando
```bash
  pytest -v -m smoketests
```

Para generar un reporte allure, se debe ejecutar en consola el siguiente comando: 
```bash
  py.test --alluredir=reports ./tests
  
  allure serve reports
```
