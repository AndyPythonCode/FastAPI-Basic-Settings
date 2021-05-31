# FASTAPI FRAMEWORK

# Database
    he creado una conexion usando SQLAlchemy ORM de manera asincrona

# apps/manage.py
    esta va hacer mi lista de comando, hasta el momento solo cuenta con una:

* ## __python apps/manage.py --app [name]
    se utiliza para crear una nueva aplicacion con una estructura de ejemplo.

# Plugin 
* ## __execute_models:__ con esto logro podrer buscar en la carpeta apps en cada carpeta el archivo models.py.
    ¿Que logro con esto?
    Bueno de esta manera me simplifico bastante, de tal modo que si quiero crear otras rutas (es decir, nuevas api) 
    solo necesito crear otra carpeta y dentro de ella creo un models.py y ya mis nuevas tablas se veran reflejada dentro
    del mismo
* ## __example:__ esta es la estructura que yo necesito seguir cuando create una nueva app
    Me simplifico bastante, de esa manera ahorro tiempo escribiendo la misma estructura.

# Paquetes
    * pip install databases[sqlite]
        - aiosqlite
        - SQLAlchemy
    * pip install uvicorn
    * pip install fastapi

# vercel.json
* para hacer un despliegue en la plataforma de vercel, solo instala la __CLI vercel__ y ejecuta el commando __vercel .__