from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the Pydantic model
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: float = 0.0

# published must be a boolean value (True or False).
# float → This means the field expects a decimal number (like 3.5, 4.0, 10.75)If client forgets published, it will still be True.

# If client forgets rating, it will be 0.0

# If the user sends something else (like a string "yes"), FastAPI will try to convert it, or if it can’t, it will reject the request with a validation error.
# POST endpoint using Pydantic model
@app.post("/createposts")
def create_posts(new_post: Post):
    # Access the data via dot notation
    print(new_post.title)      # prints the title to the server console
    print(new_post.content)    # prints the content to the server console

    # Return the data as JSON
    return {
        "title": new_post.title,
        "content": new_post.content
    }
# Pydantic is a Python library used for data validation and parsing.

# It lets you define data models (schemas) using Python classes.

# Behind the scenes, it makes sure the input data matches the expected types and structure.

# If the data doesn’t match, Pydantic raises clear validation errors.

# Why use Pydantic in FastAPI?

# FastAPI is built around Pydantic models because they give you:

# Validation – Ensures client input (from Postman, frontend, etc.) has the right fields and types.

# class Post(BaseModel):
#     title: str
#     content: str


# If a client sends {"title": 123, "content": "Hello"}, FastAPI will return an error automatically.

# Without Pydantic, you’d need to write manual checks.

# If a client sends {"title": 123, "content": "Hello"}, FastAPI will return an error automatically.

# Without Pydantic, you’d need to write manual checks.

# Type Safety – Your editor (VSCode, PyCharm, etc.) will auto-suggest .title, .content, etc.
# With plain dicts, you can accidentally mistype "titel" instead of "title", and Python won’t catch it.

# Automatic Docs (Swagger UI) – When you use Pydantic models, FastAPI generates:

# /docs (Swagger UI)

# /redoc (ReDoc UI)
# Both show expected request body structure directly from your model.

# Example:
# Serialization & Parsing – Pydantic converts data automatically:

# JSON → Python object

# Python object → JSON

# Clean Code – Instead of working with raw dicts, you work with structured objects:

# def create_post(post: Post):
#     return post.dict()

# PYDANTIC AND SCHEMA
# 1. Schema Definition

# When you create a BaseModel in Pydantic, you’re actually defining a data schema.
# For example:

# from pydantic import BaseModel

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True


# This is both a Python class and a schema:

# title must be a string

# content must be a string

# published must be a boolean (default True)

# If your incoming data doesn’t match this, FastAPI automatically rejects it with a clear error message.

# 2. Validation

# If the client sends bad data like:

# {
#   "title": 123,
#   "content": true
# }


# FastAPI will respond with:

# {
#   "detail": [
#     {
#       "loc": ["body", "title"],
#       "msg": "str type expected",
#       "type": "type_error.str"
#     },
#     {
#       "loc": ["body", "content"],
#       "msg": "str type expected",
#       "type": "type_error.str"
#     }
#   ]
# }


# So you don’t need to manually check data types.

# 3. Automatic Schema Docs (OpenAPI/Swagger)

# FastAPI uses Pydantic models to generate API schemas automatically.
# If you go to:

# http://127.0.0.1:8000/docs → Swagger UI

# http://127.0.0.1:8000/redoc → ReDoc

# You’ll see your Post model clearly documented as part of your API.

# 4. Data Conversion

# Pydantic can even convert types when possible:

# post = Post(title="My Post", content="Hello", published="true")
# print(post.published)   # True (auto converted to bool)


# 👉 In short:

# Dict = flexible, but no rules.

# Pydantic model = structured, validated, documented schema.


# WHAT IS PAYLOAD/NEWPOST
# In Postman, when you send data in the request body (usually as JSON), that data becomes:

# payLoad if your function parameter is defined as payLoad: dict = Body(...).

# new_post if your function parameter is defined as new_post: Post (using a Pydantic model).

# So:

# 🔹 Dict example (maindict.py)

# from fastapi import FastAPI, Body

# app = FastAPI()

# @app.post("/createposts")
# def create_posts(payLoad: dict = Body(...)):
#     return {
#         "title": payLoad["title"],
#         "content": payLoad["content"]
#     }


# 👉 In Postman, when you send:

# {
#   "title": "My first post",
#   "content": "FastAPI is amazing"
# }


# That JSON becomes payLoad.

# 🔹 Pydantic example (mainpydantic.py)

# from fastapi import FastAPI
# from pydantic import BaseModel

# class Post(BaseModel):
#     title: str
#     content: str

# app = FastAPI()

# @app.post("/createposts")
# def create_posts(new_post: Post):
#     return {
#         "title": new_post.title,
#         "content": new_post.content
#     }


# 👉 In Postman, you send the same JSON:

# {
#   "title": "My first post",
#   "content": "FastAPI is amazing"
# }


# That JSON becomes new_post, but here it’s a Pydantic model instead of a raw dict.

# ✅ Key difference:

# With dict, you manually pull values using keys (payLoad["title"]).

# With Pydantic, you access values as attributes (new_post.title) and get validation for free.



# PYDANTIC MODE
# 1. What is a Pydantic model?

# A Pydantic model is a Python class that inherits from BaseModel (from the pydantic library).

# Example:

# from pydantic import BaseModel

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True


# Here Post is a Pydantic model.

# It defines the schema (the structure and data types) for your data.

# It also provides validation (e.g., if you send an integer instead of a string for title, FastAPI will reject it).

# 2. How FastAPI uses it

# When you write something like this:

# @app.post("/createposts")
# def create_posts(payload: Post):
#     return payload


# FastAPI reads payload: Post and thinks:

# “Oh! The request body must follow the schema of the Post Pydantic model.”

# So it expects JSON like:

# {
#   "title": "My First Post",
#   "content": "This is the content",
#   "published": true
# }


# If you send:

# {
#   "title": 123,
#   "content": "Text here"
# }


# 👉 FastAPI will reject it with a validation error, because title is not a string (as defined in the Post model).

# 3. Why is it powerful?

# Schema definition → You define the structure once in Python code.

# Validation → Automatically checks data types.

# Documentation → FastAPI generates Swagger docs for you at http://127.0.0.1:8000/docs.

# ✅ So when I said “Expect this body to match the Post Pydantic model”, I meant:
# FastAPI will only accept request data if it matches the structure and types you defined in the Post model.

