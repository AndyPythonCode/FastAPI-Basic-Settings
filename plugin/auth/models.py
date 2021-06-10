# Create you own tables inside database.
import sqlalchemy
from database.db import metadata

user = sqlalchemy.Table("user",
	metadata,
	sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
	sqlalchemy.Column("username", sqlalchemy.String(255)),
	sqlalchemy.Column("full_name", sqlalchemy.String(255)),
	sqlalchemy.Column("email", sqlalchemy.String(80)),
	sqlalchemy.Column("hashed_password", sqlalchemy.String(255)),
	sqlalchemy.Column("disabled", sqlalchemy.Boolean),
)

revoked_token = sqlalchemy.Table("revoked_token", 
	metadata, 
	sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
	sqlalchemy.Column("token", sqlalchemy.String(255)),
)