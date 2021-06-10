from database.db import database
from ..auth.schemas import UserAdmin
from ..auth.encrypt import get_password_hash
from ..auth.models import user

async def dropTable(table: str):
    return await database.execute(f'DROP TABLE {table};')

async def createsuperuser():
    form = {
        'username': '',
        'email': '',
        'full_name': '',
        'hashed_password': '',
    }
    form['username'] = input("\n\nusername: ")
    form['email'] = input("email: ")
    form['full_name'] = input("full_name: ")
    form['hashed_password'] = get_password_hash(input("hashed_password: "))

    userIn = UserAdmin(**form)
    query = user.insert().values(**userIn.dict())
    await database.execute(query)
    print('User admin created!!!')