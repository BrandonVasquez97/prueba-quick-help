# Pasos para correr la aplicación
Tener en cuenta que la Base de datos no es necesario montarla pues esta en la nube montada en una RDS en AWS, igual hay sql de su estructura, el usuario y la contraseña fue compartida en el correo

# Clonar repositorio
En la terminal del git bash clonan con el siguiente comando: 

git clone https://github.com/BrandonVasquez97/prueba-quick-help.git

Despues acceden a la carpeta:

cd prueba-quick-help

A partir de ahi pueden acceder al repositorio en el visual studio con el comando: 

code .

# Correr la aplicación Dentro del Visual Studio
Ya dentro del visual se abre una nueva terminal en cmd, no se recomienda usar la de powershell
(Asumiendo que se tenga instalado Python 3.9)

Crean un entorno virtual con:

python -m venv env

activan el entorno virtual con:

.\env\scripts\activate

Instalan las dependencias:

pip install -r requirements.txt

acceden a la carpeta del proyecto django:

cd Proyecto_Quick

corren el proyecto con el comando:

python manage.py runserver

sabran que funciono si en la terminal aparece:

Starting development server at http://127.0.0.1:8000/

# Consumir las APIs
Importan en el postman el proyecto adjuntado en el correo con el nombre de prueba-quick.postman_collection

Tener en cuenta que el proyecto en postman esta dividido en 5 carpetas: Products, Bills, Clients, CSV, Usuario

Las carpetas Products, Bills y Clients tienen las operaciones CRUD de esas entidades

La carpeta CSV contiene las apis para generar y cargar el CSV

La carpeta Usuario tiene para loguear y crear usuario

Es necesario loguearse para usar las apis, con la api de loguear usuario podran acceder y retornara un token el cual se debe colocar para las demas apis en el cuerpo de la peticion, estara especificado con la clave "token"

Importante a tener en cuenta que todas las apis estan diseñadas para que la peticion se haga con un JSON en la opcion Body-raw del postman, la unica exepcion es la api de cargar CSV que se diseño con un form-data con dos KEY una llamada csv_file y otra token, en el VALUE para csv_file podran subir el archivo y el VALUE del token debe estar el token entregado al loguearse

# Archivos CSV
Los CSV que se generen se almacenan en la carpeta CSV_generados, dentro de la carpeta del proyecto django Proyecto_Quick

# Cargando el CSV
Ya explicado como consumir esta api, tener en cuenta que en el proyecto hay una plantilla llamada plantilla_cargue_de_clientes.csv para que funcione correctamente el cargue del documento se debe seguir el formato de esa plantilla donde la primera fila sera el encabezado y las demas podran colocar los datos del cliente

