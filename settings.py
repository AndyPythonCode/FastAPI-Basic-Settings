import apps
from fastapi.applications import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from plugin.auth.routers import router_auth

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
    if AUTH:
        app.include_router(router_auth)

# SECURITY https://fastapi.tiangolo.com/tutorial/cors/
MIDDLEWARE = {
    'middleware_class': CORSMiddleware,
    'allow_origins': ['*'],
    'allow_credentials': True,
    'allow_methods': ["*"],
    'allow_headers': ["*"],
}

# AUTH # https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
AUTH = True

# to get a string like this run: openssl rand -hex 32
SECRET_KEY = "b616f87bace1bf9f1e511a9f939046846c909f550538725292f2c2d33a9b7c80"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_HOURS = 12