# API Python Flask
API Test Softpymes, con manejo de excepciones, manejo de base de datos MySQL
desarrollada en lenguaje Python, framework Flask y ORM SqlAlchemy


## Requerimientos

Se requiere tener instalados:
- Python versiones 3 superiores a 3.6 
- virtualenv
- IDE pycharm (opcional)

## Instalación
Instalación de recursos

### Creación del Entorno
Para la creación del entorno virtual se deben ejecutar los siguientes comandos:
```
pyhton -m venv venv
```

### Instalar Requerimientos
```
source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirenments.txt
```

### Ejecutar API
Ejecutar: Los comandos a continuación permitirán la ejecución de la API
```
python run.py
```

### Probar la API - POSTMAN
```
http://127.0.0.1:5000/api/v1/index
```

# Objetivo de la Prueba

La prueba consiste en realizar un CRUD completo para el módulo de Example, lo cual se divide en los siguientes puntos:

1. Se requiere CONSULTAR todos los registros de la tabla.
2. Se requiere CONSULTAR todos los registros de la tabla por id.
3. Se require CONSULTAR todos los registros de la tabla de manera paginada y consultar por un criterio de busqueda.
4. Se require GUARDAR un registro en la tabla.
5. Se requiere ACTUALIZAR todos la información de un registro especifico..
6. Se require ELIMINAR un registro especifico.



