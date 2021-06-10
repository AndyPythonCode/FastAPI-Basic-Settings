from passlib.context import CryptContext # passlib[bcrypt] es un gran paquete de Python para manejar hashes de contraseñas.

# Esto es lo que se utilizará para hacer hash y verificar las contraseñas.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Verificar si la contraseña coincide con la digitada por el usuario
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Encriptar la contraseña
def get_password_hash(password):
    return pwd_context.hash(password)