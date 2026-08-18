from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.database import get_db, Base
from app.main import app
from app import schemas
from app.config import settings
from alembic.config import Config
from alembic import command


# SQLALCHEMY_DATABASE_URL = f'postgresql://{'postgres:postgres123@localhost:5432/fastapi_test'}'

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'


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


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base.metadata.create_all(bind=engine)
# THIS tells SQLALchemy create all tables defined in my models if they don't already exist."
# Base = declarative_base()


# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# app.dependency_overrides[get_db] = override_get_db

# client = TestClient(app)
@pytest.fixture()
def session():
    print("run my session fixture")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
            db.close()
    

@pytest.fixture ()
def client(session):
    def override_get_db():
    
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
# This means, Whenever an endpoint asks for get_db, give it this test session.

    yield TestClient(app)
   