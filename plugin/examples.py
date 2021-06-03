# structure for python manage.py --app <name>

def models(command: str):
    model = {'example': '# Create you own tables inside database.\n\n' +
             'import sqlalchemy \n' +
             'from database.db import metadata\n\n' +
             f'{command} = sqlalchemy.Table(' +
             f'"{command}", \n' +
             '\tmetadata, \n' +
             '\tsqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),\n' +
             '\tsqlalchemy.Column("text", sqlalchemy.String(255)),\n' +
             '\tsqlalchemy.Column("completed", sqlalchemy.Boolean),\n' +
             ')'
             }
    return model['example']


def routers(command: str):
    router = {'example': '# Validate everydata that get in.\n\n' +
              'from fastapi import APIRouter\n\n' +
              f'router_{command} = APIRouter(\n' +
                  f'\tprefix="/{command}",\n'+
                  f'\ttags=["{command.capitalize()}"]\n'+
              ')\n\n'+
              f'@router_{command}.get("/")\n' +
              f'def Home_{command.capitalize()}(): \n' +
	          '\treturn {"Hello":"World"}'}
    return router['example']


def schemas(command: str):
    schema = {'example': '# Create you own path.\n\n' +
              'from pydantic import BaseModel\n' +
              'from typing import Optional\n\n' +
              f'class Schemas{command.capitalize()}(BaseModel):\n' +
              '\ttext: str\n' +
              '\tcompleted: Optional[bool]\n'
              }
    return schema['example']