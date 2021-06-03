import databases #Async database support for Python.
import sqlalchemy #ORM

# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite:///database/sql_app.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"
# DATABASE_URL = "mysql://user:password@postgresserver/db"

# we are "connecting" to a SQLite database (opening a file with the SQLite database).
database = databases.Database(DATABASE_URL)

# The MetaData is a registry which includes the ability to emit a 
# limited set of schema generation commands to the database.
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL, 
    # it is needed only for SQLite. It's not needed for other databases.
    connect_args={"check_same_thread": False}
)

"""
### connect_args={"check_same_thread": False}

By default SQLite will only allow one thread to communicate with it, assuming that each 
thread would handle an independent request. This is to prevent accidentally sharing the 
same connection for different things (for different requests).

But in FastAPI, using normal functions (def) more than one thread could interact with 
the database for the same request, so we need to make SQLite know that it should allow 
that with connect_args={"check_same_thread": False}.

Also, we will make sure each request gets its own database connection session in a 
dependency, so there's no need for that default mechanism.
"""
