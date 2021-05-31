import apps
import settings
from fastapi import FastAPI
from database.db import metadata, engine, database

app = FastAPI(title='Tech With Tim', version='0.0.1')

# Run every models in folder apps
settings.MODELS()

# Create the database tables
metadata.create_all(engine)

#Adding routers
settings.URL_PATTERNS(apps.ROUTERS_APPS, app)

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()