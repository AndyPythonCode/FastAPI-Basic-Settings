# structure for python manage.py --app <name>

def models():
    model = {'example': '# Create you own tables inside database.\n\n' +
             'import sqlalchemy \n' +
             'from database.db import metadata\n\n' +
             'notes = sqlalchemy.Table(' +
             '"notes", \n' +
             '\tmetadata, \n' +
             '\tsqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),\n' +
             '\tsqlalchemy.Column("text", sqlalchemy.String),\n' +
             '\tsqlalchemy.Column("completed", sqlalchemy.Boolean),\n' +
             ')'
             }
    return model['example']


def routers():
    router = {'example': '# Validate everydata that get in.\n\n' +
              'from fastapi import APIRouter\n\n' +
              'router_note = APIRouter(\n' +
                  '\tprefix="/note",\n'+
                  '\ttags=["Note"]\n'+
              ')\n\n'+
              '# @router_note.get("/")\n'}
    return router['example']


def schemas():
    schema = {'example': '# Create you own path.\n\n' +
              'from pydantic import BaseModel\n' +
              'from typing import Optional\n\n' +
              'class SchemasNotes(BaseModel):\n' +
              '\ttext: str\n' +
              '\tcompleted: Optional[bool]\n'
              }
    return schema['example']