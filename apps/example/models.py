# Create you own tables inside database.

import sqlalchemy 
from database.db import metadata

notes = sqlalchemy.Table("notes", 
	metadata, 
	sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
	sqlalchemy.Column("text", sqlalchemy.String),
	sqlalchemy.Column("completed", sqlalchemy.Boolean),
)