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
    Esta va hacer mi lista de comando para facilitar ciertas tareas:

1. ### __python manage.py --app [name]__
    Se utiliza para crear una nueva aplicacion con una estructura de ejemplo.

2. ### __python manage.py --drop [table_name]__
    Se utiliza para eliminar una tabla en la base de datos

2. ### __python manage.py --createsuperuser__
    Se utiliza para crear un admin en la base de datos, es decir, (disabled=True)

# settings
    Aquí hay una lista de configuraciones disponibles en el núcleo

# Plugin 
    Los plugins son pequeños programas complementarios que amplían las funciones de aplicaciones

1. __Data:__ esta es la estructura que yo necesito seguir cuando create una nueva app
    Me simplifico bastante, de esa manera ahorro tiempo escribiendo la misma estructura.

2. __Auth:__ la generacion de una autentificacion, esto me permite colocarle candado a ciertas rutas.
    Podras utilizar las rutas siempre y cuando mandes el token de verificacion

1. __db:__ ddl: trabajar con la estructura de la base de datos. dml: podrer hacer un crud de manera sencilla,
    ya que esta implementado solo se necesita crear un objeto y cumplir con la espeficicaciones

# Paquetes instalados default
    Paquetes ya instalados.

* pip install databases[sqlite]
    * aiosqlite
    * SQLAlchemy
* pip install uvicorn
* pip install fastapi
* pip install python-multipart
* pip install python-jose[cryptography]
* pip install passlib[bcrypt]
* pip install pydantic[email]

# vercel.json
    Vercel es una plataforma en la nube para sitios estáticos y funciones sin servidor que se adapta perfectamente a su flujo de trabajo. 

* para hacer un despliegue en la plataforma de vercel, solo instala la __CLI vercel__ y ejecuta el commando __vercel .__ siempre cuando tengas un requirements.txt en la raiz.