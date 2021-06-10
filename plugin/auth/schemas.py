# Create you own path.
from typing import Optional
from pydantic import BaseModel, EmailStr

# Especificar cual va hacer la salida
class Token(BaseModel):
    access_token: str
    token_type: str

# Devolver un objeto token
class TokenData(BaseModel):
    username: Optional[str] = None

# Devolver un objeto user
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

# Devolver un objeto password hash
class UserInDB(User):
    hashed_password: str

#Crear un objeto User
class UserForm(BaseModel):
	username: str
	email: EmailStr
	full_name: str
	hashed_password: str

class UserIn(UserForm):
	disabled: bool = False

class UserAdmin(UserForm):
    disabled: bool = True