# from fastapi.testclient import TestClient
# import pytest
# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
# from app.database import get_db, Base
# from app.main import app
# from app import schemas
# from app.config import settings
# from alembic.config import Config
# from alembic import command


# # SQLALCHEMY_DATABASE_URL = f'postgresql://{'postgres:postgres123@localhost:5432/fastapi_test'}'

# SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'


# print(SQLALCHEMY_DATABASE_URL)
# # engine = create_engine(
# #     SQLALCHEMY_DATABASE_URL,
# #     pool_pre_ping=True


# # )

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     pool_pre_ping=True,      # Prevents stale connections
#     pool_size=5,             # Keep this small for development
#     max_overflow=10,
#     pool_timeout=30,
#     echo=False               # Set True only for debugging
# )


# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base.metadata.create_all(bind=engine)
# # THIS tells SQLALchemy create all tables defined in my models if they don't already exist."
# # Base = declarative_base()


# # def override_get_db():
# #     db = TestingSessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()

# # app.dependency_overrides[get_db] = override_get_db

# # client = TestClient(app)
# @pytest.fixture
# def session():
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#             db.close()
    

# @pytest.fixture
# def client(session):
#     def override_get_db():
    
#         try:
#             yield session
#         finally:
#             session.close()
#     app.dependency_overrides[get_db] = override_get_db
# # This means, Whenever an endpoint asks for get_db, give it this test session.

#     yield TestClient(app)
   

# def test_root(client):
#     res = client.get("/",)
#     print(res.json())
#     assert res.json().get("message") == "Hello Jossy, welcome back to this class"
#     assert res.status_code == 200
#     # return {"m essage": "Hello Jossy, welcome back to this class"}

# def test_create_user(client):
#     res = client.post("/users", json = {"email":"userhell02@gmail.com", "password":"password2", "residence": "Nakuru"})
#     new_user = schemas.UserOut(**res.json())
#     print(new_user)
#     assert new_user.email == "userhell02@gmail.com"
#     print(res.json())
#     assert res.status_code == 201



    
#     # allows us to run our cide vefore we run our test 
    
#     # command.upgrade("head")
#     # yield TestClient(app)
#     # # command.downgrade("base")
#     # # run our code after the test finishes



#     # ///////////////////////////////////
# #     Question 1

# # What is the main purpose of TestClient?

# # A. It starts a PostgreSQL database.

# # B. It allows your tests to send HTTP requests to your FastAPI application without running Uvicorn.

# # C. It creates SQLAlchemy models.

# # D. It runs Alembic migrations.

# # ✅ Answer

# # B

# # 📖 Explanation

# # TestClient behaves like a web browser or Postman inside your test. It sends requests such as:

# # response = client.get("/")

# # or

# # response = client.post("/users", json=data)

# # without needing to start the FastAPI server using uvicorn.

# # Question 2

# # Consider the following code:

# # engine = create_engine(SQLALCHEMY_DATABASE_URL)

# # TestingSessionLocal = sessionmaker(bind=engine)

# # What connects TestingSessionLocal to the fastapi_test database?

# # A. sessionmaker()

# # B. bind=engine

# # C. TestingSessionLocal()

# # D. yield

# # ✅ Answer

# # B

# # 📖 Explanation

# # The engine is already connected to:

# # postgresql://.../fastapi_test

# # When you write

# # TestingSessionLocal = sessionmaker(bind=engine)

# # every session created by TestingSessionLocal() automatically uses that engine, and therefore the fastapi_test database.

# # Flow:

# # TestingSessionLocal
# #         │
# #         ▼
# #       Engine
# #         │
# #         ▼
# #  fastapi_test
# # Question 3

# # Why do we override get_db() during testing?

# # A. To make tests run faster.

# # B. To ensure the API uses the testing database session instead of the normal database.

# # C. To encrypt passwords.

# # D. To create tables.

# # ✅ Answer

# # B

# # 📖 Explanation

# # Normally, your endpoint does this:

# # db: Session = Depends(get_db)

# # During testing, we replace get_db() with override_get_db() so every endpoint uses the testing database rather than your development database.

# # Question 4

# # What does this line do?

# # app.dependency_overrides[get_db] = override_get_db

# # A. Deletes get_db.

# # B. Replaces get_db during testing.

# # C. Creates a new database.

# # D. Creates SQLAlchemy models.

# # ✅ Answer

# # B

# # 📖 Explanation

# # FastAPI has a dictionary called dependency_overrides.

# # Normally:

# # Depends(get_db)
# #         │
# # Production Database

# # After overriding:

# # Depends(get_db)
# #         │
# # override_get_db()
# #         │
# # Testing Database

# # Only the dependency changes—the endpoint code stays exactly the same.

# # Question 5

# # Why do pytest fixtures use yield instead of return?

# # A. yield is faster.

# # B. yield pauses the fixture so cleanup can happen after the test.

# # C. return is not allowed.

# # D. There is no difference.

# # ✅ Answer

# # B

# # 📖 Explanation

# # With return:

# # Setup
# #    │
# # Return
# #    │
# # Function ends

# # With yield:

# # Setup
# #    │
# # Yield
# #    │
# # Run Test
# #    │
# # Cleanup

# # This makes yield perfect for opening and later closing resources like database sessions.

# # Question 6

# # When does this execute?

# # db.close()
# # @pytest.fixture
# # def session():
# #     db = TestingSessionLocal()

# #     try:
# #         yield db
# #     finally:
# #         db.close()

# # A. Before the test.

# # B. During the test.

# # C. After the test.

# # D. Never.

# # ✅ Answer

# # C

# # 📖 Explanation

# # Execution pauses at:

# # yield db

# # The test runs.

# # When the test finishes, execution resumes and:

# # db.close()

# # is executed.

# # Question 7

# # Given:

# # @pytest.fixture
# # def session():
# #     ...

# # @pytest.fixture
# # def client(session):
# #     ...

# # Which fixture runs first?

# # A. client

# # B. session

# # C. Both together

# # D. Randomly

# # ✅ Answer

# # B

# # 📖 Explanation

# # The client fixture depends on session.

# # Pytest sees:

# # client(session)

# # and knows:

# # session
# #    │
# # client
# #    │
# # test

# # Pytest automatically resolves the dependency.

# # Question 8

# # Why did your teacher split the fixtures?

# # A. Pytest only allows one job per fixture.

# # B. To give each fixture a single responsibility.

# # C. SQLAlchemy requires it.

# # D. There is no reason.

# # ✅ Answer

# # B

# # 📖 Explanation

# # The session fixture only manages the database.

# # The client fixture only manages the TestClient and dependency override.

# # This makes both fixtures easier to understand and reuse.

# # Question 9

# # What is the job of this fixture?

# # @pytest.fixture
# # def client(session):

# # A. Create the database.

# # B. Receive a session, override get_db, and create a TestClient.

# # C. Drop all tables.

# # D. Create SQLAlchemy models.

# # ✅ Answer

# # B

# # 📖 Explanation

# # The database has already been prepared by the session fixture.

# # The client fixture simply says:

# # "Whenever FastAPI asks for a database session, use this testing session."

# # Then it creates the TestClient.

# # Question 10

# # Why create a separate database called fastapi_test?

# # A. It is faster.

# # B. To protect your development database.

# # C. FastAPI requires it.

# # D. PostgreSQL requires it.

# # ✅ Answer

# # B

# # 📖 Explanation

# # Tests insert, update and delete data.

# # You never want your tests modifying your real application database.

# # Using a dedicated test database keeps your development data safe.

# # Question 11

# # What is a pytest fixture?

# # A. A unit test.

# # B. Reusable setup and cleanup code.

# # C. A SQLAlchemy model.

# # D. A FastAPI route.

# # ✅ Answer

# # B

# # 📖 Explanation

# # A fixture prepares something that tests need.

# # Examples include:

# # a database session
# # a logged-in user
# # a TestClient
# # an authorization token

# # Fixtures eliminate repeated setup code.

# # Question 12

# # How does pytest know what to pass into this fixture?

# # @pytest.fixture
# # def client(session):

# # A. It asks FastAPI.

# # B. It looks for another fixture called session.

# # C. It checks .env.

# # D. It creates a new variable.

# # ✅ Answer

# # B

# # 📖 Explanation

# # Pytest matches fixture names.

# # When it sees:

# # def client(session):

# # it searches for:

# # @pytest.fixture
# # def session():

# # runs it, gets the yielded value, and passes that value into client() automatically.


# # Your fixture is:

# # @pytest.fixture
# # def sample():
# #     print("1. Setup")

# #     yield "Hello"

# #     print("2. Cleanup")

# # Your test is:

# # def test_example(sample):
# #     print("3. Test")

# # Here's what pytest does internally:

# # Step 1: Pytest looks at the test

# # It sees:

# # def test_example(sample):

# # and thinks:

# # "This test needs a fixture called sample. I have to create it before I can run the test."

# # Step 2: Pytest starts the fixture

# # It begins executing sample().

# # print("1. Setup")

# # Output:

# # 1. Setup

# # Then it reaches:

# # yield "Hello"

# # At this point:

# # "Hello" is given to the test as the value of sample.
# # The fixture pauses.
# # Step 3: Pytest runs the test

# # Now the test starts:

# # def test_example(sample):
# #     print("3. Test")

# # Output:

# # 3. Test
# # Step 4: Pytest resumes the fixture

# # After the test finishes, pytest goes back to the fixture and continues after the yield:

# # print("2. Cleanup")

# # Output:

# # 2. Cleanup

# # So the complete output is:

# # 1. Setup
# # 3. Test
# # 2. Cleanup
# # Why can't the test run first?

# # Imagine the fixture is creating a database connection:

# # @pytest.fixture
# # def db():
# #     print("Opening database")
# #     yield Database()
# #     print("Closing database")

# # and your test is:

# # def test_users(db):
# #     db.query(...)

# # If pytest ran the test first, the variable db wouldn't exist yet.

# # It would be like trying to drive a car before it's been built.

# # The order has to be:

# # Create database
# #        ↓
# # Run test
# #        ↓
# # Close database
# # A helpful analogy

# # Think of going to a restaurant.

# # The fixture is the waiter preparing your table:

# # Set the table
# #       ↓
# # Seat the customer
# #       ↓
# # Customer eats
# #       ↓
# # Clear the table

# # The customer (the test) can't eat before the table has been prepared.

# # That's exactly how fixtures work:

# # Setup
# #    ↓
# # Test
# #    ↓
# # Cleanup
# # Quick check for you

# # What do you think this prints?

# # import pytest

# # @pytest.fixture
# # def number():
# #     print("Creating number")
# #     yield 10
# #     print("Destroying number")

# # def test_math(number):
# #     print(number * 2)

# # A.

# # 20
# # Creating number
# # Destroying number

# # B.

# # Creating number
# # 20
# # Destroying number

# # C.

# # Creating number
# # Destroying number
# # 20

# # D.

# # Destroying number
# # Creating number
# # 20

# # Try answering before looking back at the explanati