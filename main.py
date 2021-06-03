import settings
from fastapi import FastAPI
from database.db import metadata, engine, database

#Init
app = FastAPI(**settings.API_METADATA)

# Create the database tables
metadata.create_all(engine)

# CORS (Cross-Origin Resource Sharing)
app.add_middleware(**settings.MIDDLEWARE)

#Adding routers
settings.URL_PATTERNS(app)

#Every get in
@app.on_event('startup')
async def startup():
    await database.connect()

#Every get out
@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()