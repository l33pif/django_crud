# django crud
Se debe desarrollar un REST API que permita realizar operaciones CRUD en las entidades de Cliente, Facturas y Productos


Creamos un entorno virtaul donde instalamos django
empezamos un projecto y tambien creamos una aplicacion 

Tenemos wue modificar el archivo settings para agregar nuestra nueva app
en 'INSTALLED APP' tambien instalamos djangorestframework y la agregamos en
esta lista como rest_framework

conectaremos postgreSQL con django para eso instalmos psycopg2-binary
y crearemos una database en pgadmin.
detro el archivo settings modificamos el objeto DATABASES y colocamos nuestra
informacion de postgresql

hacemos una migracion para los modelos que estan por default y podremos ver 
las tablas en pdadmin

dentro de models.py creamos las clases que ocuparemos con sus atributos
para que aparezcan en la base de datos tenemos que hacer una migracion

usaremos serializer para definir la conversion de datos de json-python
creamos un archivo de viewsets
creamos un archivo routes donde registraremos las rutas con los viewsets
en el archivo urls definiremos las rutas

si corremos el servidor y vamos a la url en postman, podremos ver que podremos hacer
GET, POST, PUT, DELETE.
