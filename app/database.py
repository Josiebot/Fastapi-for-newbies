from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
# import time
from .config import settings
#  connection string
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres123@localhost/fastapi"
# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-adress/hostname>/<database_name>/'
# 
# ['SQLALCHEMY_DATABASE_URI'] = "postgresql://username:password@localhost:port/DBNAME".
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
print(SQLALCHEMY_DATABASE_URL)
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     pool_pre_ping=True


# )

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,      # Prevents stale connections
    pool_size=5,             # Keep this small for development
    max_overflow=10,
    pool_timeout=30,
    echo=False               # Set True only for debugging
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



# engine is responsible for sqlalchemy to connect to a postgresdatabase

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create_engine → main function to set up the connection between your Python app and the database (PostgreSQL in your case).

# Think of it as building the "bridge" to your database.

# DECLARATIVE BASE
# declarative_base → gives you a base class to define models (tables).
# You’ll later do something like: All models inherit from Base so SQLAlchemy knows how to map them to actual database tables.

# SESSIONMAKER
# sessionmaker → creates a factory for database sessions.

# A session = one conversation with the database (open a connection, run queries, then close it).