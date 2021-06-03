<h1 align="center">
    <em>FastAPI Framework, Structure</em>
</h1>

<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://i.ibb.co/ZTgxXGp/python.jpg" alt="FastAPI"></a>
</p>

# Database
    He creado una conexion usando SQLAlchemy ORM de manera asincrona

* Sqlite: 
    * default
* Postgresql: 
    * pip install databases[postgresql]
* Mysql: 
    * pip install databases[mysql]
    * pip install mysqlclient

# apps folder
    Incluye cada aplicacion nueva creada
    
* __init file__: este archivo contiene ROUTERS_APPS, cuando creas una aplicacion nueva (folder) solo tiene que incluir 
el respectivo folder adentro de la tupla.

# manage
    Esta va hacer mi lista de comando, hasta el momento solo cuenta con una:

1. ### __python apps/manage.py --app [name]__
    Se utiliza para crear una nueva aplicacion con una estructura de ejemplo.

# settings
    Aquí hay una lista de configuraciones disponibles en el núcleo

# Plugin 
    Los plugins son pequeños programas complementarios que amplían las funciones de aplicaciones

1. __example:__ esta es la estructura que yo necesito seguir cuando create una nueva app
    Me simplifico bastante, de esa manera ahorro tiempo escribiendo la misma estructura.

# Paquetes instalados default
    Paquetes ya instalados.

* pip install databases[sqlite]
    * aiosqlite
    * SQLAlchemy
* pip install uvicorn
* pip install fastapi

# vercel.json
    Vercel es una plataforma en la nube para sitios estáticos y funciones sin servidor que se adapta perfectamente a su flujo de trabajo. 

* para hacer un despliegue en la plataforma de vercel, solo instala la __CLI vercel__ y ejecuta el commando __vercel .__