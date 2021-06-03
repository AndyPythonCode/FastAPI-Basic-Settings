import apps
from fastapi.applications import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# DESCRIPTION
API_METADATA = {
    'title': 'Init',
    'description': 'Welcome to FastAPI',
    'version': '0.0.1',
    'docs_url':'/', #by default it's /docs
}

#Path API added in apps
def URL_PATTERNS(app: FastAPI) -> None:
    for router in apps.ROUTERS_APPS:
        app.include_router(router)

# SECURITY https://fastapi.tiangolo.com/tutorial/cors/
MIDDLEWARE = {
    'middleware_class': CORSMiddleware,
    'allow_origins': ['*'],
    'allow_credentials': True,
    'allow_methods': ["*"],
    'allow_headers': ["*"],
}