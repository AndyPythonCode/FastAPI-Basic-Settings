# Create you own tables inside database.

import sqlalchemy 
from database.db import metadata

example = sqlalchemy.Table("example", 
	metadata, 
	sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
	sqlalchemy.Column("text", sqlalchemy.String(255)),
	sqlalchemy.Column("completed", sqlalchemy.Boolean),
)