import settings
from typing import Optional
from jose import JWTError, jwt # Necesitamos instalar python-jose[cryptography] para generar y verificar los tokens JWT en Python
from datetime import datetime, timedelta
from .encrypt import verify_password, get_password_hash # passlib[bcrypt]
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm # módulo que simplifican el uso de mecanismos de seguridad
from .schemas import UserForm, UserInDB, Token, TokenData, UserIn
from .models import revoked_token, user
from database.db import database

router_auth = APIRouter(
		prefix='/auth',
		tags=['Authentication']
)

# Modulo que trae por defecto para la seguridad
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

async def get_user(username: str):
	query = user.select().where(user.c.username == username)
	item = await database.fetch_one(query)
	if item:
		# Hereda de User y devuelve un objeto completo
		return UserInDB(**item)

async def get_token_blackList(token: str):
	query = revoked_token.select().where(revoked_token.c.token == token)
	item = await database.fetch_one(query)
	if item:
		return True

# confirmar si existe un usuario con los datos proporcionado
async def authenticate_user(username: str, password: str):
    user = await get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(to_encode: dict, expires_delta: Optional[timedelta] = None):
    # fecha de vencimiento
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    # exp = Identifica la marca temporal luego de la cual el JWT no tiene que ser aceptado. 
    to_encode.update({"exp": expire})
	# Codificar el JWT y crear una firma y tiempo de expiracion
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
		# Decodificar el JWT y verificar si tiene una firma
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    if await get_token_blackList(token):
        raise credentials_exception    
    return user

@router_auth.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Un objeto timedelta representa una duración
    access_token_expires = timedelta(hours=settings.ACCESS_TOKEN_EXPIRE_HOURS)
    # La especificación JWT dice que hay una clave sub, con el sujeto del token
    # sub = Identifica el objeto o usuario en nombre del cual fue emitido el JWT
    access_token = create_access_token(
        to_encode={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router_auth.post("/users/create") 
async def create_user(current_user: UserForm):
	form = UserIn(**current_user.dict())
	#Encriptar password
	form.hashed_password = get_password_hash(form.hashed_password)
	query = user.insert().values(**form.dict())
	await database.execute(query)
	return {"user": "created"}

@router_auth.get("/users/me/", response_model=UserInDB)
async def read_users_me(current_user: UserInDB = Depends(get_current_user)):
    return current_user

@router_auth.get("/logout")
async def logout(token: str = Depends(oauth2_scheme)):
    # En models.py se encuentra un trigger si desea eliminar los token que exceden el tiempo
	query = revoked_token.insert().values(token=token, date=datetime.utcnow() + timedelta(hours=settings.ACCESS_TOKEN_EXPIRE_HOURS))
	await database.execute(query)
	return {'User':'Logout'}