# Ejercicios con API en Flask
## Primeros pasos
Revisa que tu versión de python sea 3.x, puedes revisarlo con el comando:
```
python -v
``` 
Instala flask con el comando:
```
pip install Flask
```
Para correr el proyecto necesitaras colocar las siguientes variables de entorno deacuerdo a tu sistema operativo:
## Unix Bash (Linux, Mac, etc.)
Asegurate estar al nivel de la carpeta en la terminal
```
export FLASK_APP=nombre_de_tu_carpeta
export FLASK_ENV=development 
flask run
```
## Windows CMD
Asegurate estar al nivel de la carpeta en la terminal
```
set FLASK_APP=nombre_de_tu_carpeta
set FLASK_ENV=development
flask run
```
## Windows PowerShell
Asegurate estar al nivel de la carpeta en la terminal
```
$env:FLASK_APP="nombre_de_tu_carpeta"
$env:FLASK_ENV="development"
flask run
```

Despues de esto la aplicación estará corriendo en el puerto 5000, para comprobarlo puedes abrir tu navegador y entrar a la siguiente dirección.
```
http://localhost:5000
```
Dentro de la carpeta encontraras un archivo llamado Ejercicios.postman_collection.json el cual podrás usar para probar los endpoint que se encuentran en la API utilizando postman.
Son 3 rutas, una por cada ejercicio, puedes encontrar las rutas en el archivo api.py en la raiz del proyecto, las funciones utilizadas en cada endpoint puedes encontrarlas dentro de la carpeta src.

## Detalles
Se encontró un error en la imagen del ejercicio Seasons Problem donde el ORD_ID 112-5230502-8173028 con fecha 1/30/20 se muestra con el resultado Summer pero con la fecha correspondiente pertenece a winter, deacuerdo con la declaración de las estaciones al inicio de la imagen.
De igual manera esto sucede con el ORD_ID 114-0291773-7262697 con fecha 12/5/19 se muestra con el resultado Winter pero con la fecha correspondiente pertenece a Fall, deacuerdo con la declaración de las estaciones al inicio de la imagen.
