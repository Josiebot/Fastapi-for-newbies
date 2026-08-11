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
from app.oauth2 import create_access_token
from app import models

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

@pytest.fixture
def test_user(client):
    user_data = {"email":"usoe@gmail.com", 
                 "password":"uso123", "residence": "Nairobi", "wrongPassword": "incorrectpassword"}

    res = client.post("/users", json = user_data)
    # assert res.status_code == 201
    print(res.json())
    print("//////////////////")
    newuser = res.json()
    print(newuser)
    newuser ['password'] = user_data['password']
    print("//////////////////////////")
    return newuser
@pytest.fixture
def test_user2(client):
    user_data = {"email":"uso34@gmail.com", 
                 "password":"uso23", "residence": "Nairobi", "wrongPassword": "incorrectpassword"}

    res = client.post("/users", json = user_data)
    # assert res.status_code == 201
    print(res.json())
    print("//////////////////")
    newuser = res.json()
    print(newuser)
    newuser ['password'] = user_data['password']
    print("//////////////////////////")
    return newuser

@pytest.fixture
def token (test_user):
     return create_access_token({"user_id": test_user['id']})
  

@pytest.fixture
def authorized_client(client, token):
     client.headers = {
          **client.headers,
          "Authorization": f"Bearer {token}"
     }

     return client

@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [{"title": "first title",
                   "content":"first content", "user_id":test_user['id']}, 

                   {"title": "2nd title",
                   "content":"2nd content", "user_id":test_user['id']}, 

                   {"title": "3rd title",
                   "content":"3rd content", "user_id":test_user['id']},
                   {"title": "3rd title",
                   "content":"3rd content", "user_id":test_user2['id']}
                   

                   ]
# USE MAP() TO CONVERT LISTS
    def create_post_model(post):
        return  models.Post(**post)

    #  map(func, posts_data)
    post_map =  map(create_post_model, posts_data)
    # Run this function on every item in the list."
    posts = list(post_map)

    session.add_all(posts)
    session.commit()
    new_posts = session.query (models.Post).all()

    return new_posts

# MANUALLY

    # session.add_all([models.Post(title="first title",
    #                 content="first content", owner_id=test_user['id']),

    #                 models.Post(title="2nd title",
    #                 content="2nd content", owner_id=test_user['id']),

    #                 models.Post(title="3rd title",
    #                 content="3rd content", owner_id=test_user['id']),])

    # session.commit()
    # posts = session.query(models.Post).all()
    # return posts




# Manually -  

# @pytest.fixture
# def test_posts(test_user, session):

#     session.add_all([
#         models.Post(
#             title="first title",
#             content="first content",
#             owner_id=test_user["id"]
#         ),

#         models.Post(
#             title="2nd title",
#             content="2nd content",
#             owner_id=test_user["id"]
#         ),

#         models.Post(
#             title="3rd title",
#             content="3rd content",
#             owner_id=test_user["id"]
#         )
#     ])

#     session.commit()

#     posts = session.query(models.Post).all()
#     return posts