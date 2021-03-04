# API Python Flask
API Test Softpymes, con manejo de excepciones, manejo de base de datos MySQL
desarrollada en lenguaje Python, framework Flask y ORM SqlAlchemy


## Requerimientos

Se requiere tener instalados:
- Python versiones 3 superiores a 3.6 
- virtualenv 
- IDE pycharm (opcional)
- Gestor de Base de Batos (MySQL)

## Instalación
Para la instalación de recursos, se debe tener en cuenta los siguientes pasos:

### Creación del Entorno
Para la creación del entorno virtual se deben ejecutar los siguientes comandos:
```
python -m venv venv
```

### Instalar Requerimientos
```
source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirenments.txt
```

### Importar la Base de Datos
Para importar la base de datos, hacer uso del script ```softpymes_test.sql``` que se encuentra en la raíz del proyecto

> **Nota:** dentro de la carpeta ```api``` existe un archivo llamado ```.env``` este archivo
> tiene la configuración para conectarse a la base de datos, modificarlo según las preferencias
> de sus equipos.

### Ejecutar API
Ejecutar: Los comandos a continuación permitirán la ejecución de la API
```
cd api
python run.py
```

### Probar la API - POSTMAN
Entre los archivos, se deja un endpoint o servicio de test, para que validen el funcionamiento del API.
```
http://127.0.0.1:5000/api/v1/index
```

# Objetivo de la prueba

La prueba consiste en realizar un CRUD completo para el módulo de Example, lo cual se divide en los siguientes puntos:

1. Se requiere CONSULTAR todos los registros de la tabla.
2. Se requiere CONSULTAR todos los registros de la tabla por ID.
3. Se requiere CONSULTAR todos los registros por un estado específico.
4. Se require CONSULTAR todos los registros de la tabla de manera paginada y consultar por cualquier criterio de búsqueda.
5. Se require GUARDAR un registro en la tabla.
6. Se requiere ACTUALIZAR toda la información de un registro específico.
7. Se require ELIMINAR un registro específico.

## Criterios de aceptación

Con el objetivo de validar el conocimiento y cumplimiento de los puntos mencionados anteriormente,
los criterios que se evaluarán son los siguientes:

1. Implementación de buenas prácticas
2. Validaciones de posibles errores, tanto de código como en resultado de las consultas
3. La forma de responder una vez se consulten los endpoint o servicios que se crearán para consumir él API
4. Creatividad enfocado a la forma de solucionar cada uno de los puntos de la prueba, las respuestas del API


## Script DATABASE

Importar el archivo con el script ```softpymes_test.sql``` se encuentra en la raíz de este proyecto


