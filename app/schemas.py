from pydantic import BaseModel
# conint
# EmailStr
from datetime import datetime
from typing import Optional
from pydantic import ConfigDict


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

# # class CreatePost(BaseModel):
# #     title:str
# #     content:str
# #     published: bool = True 

# class UpdatePost(BaseModel):
#     
#     published:bool = True

# instead of these two, we create a class called postbase
class PostNew(BaseModel):
    title:str
    content:str
    published:bool=True


class PostCreate(PostBase):
    pass

# User sending data to Us
class UserOut(BaseModel):
    id:int
    email:str
    created_at:datetime

    # class Config:
    #     orm_mode = True
    
    class Config:
        from_attributes = True


class Post(PostBase):
    id: int
    # title:str
    # content:str
    # published:bool = True (These are now inherited)
    created_at: datetime 
    user_id: int
    owner: UserOut
    # class Config:
    #     orm_mode = True
    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: str
    password:str
    residence:str




class UserLogin(BaseModel):
    email:str
    password:str
    

class Token(BaseModel):
    access_token: str
    token_type:str


class TokenData(BaseModel):
    id:Optional[int] = None


class Vote(BaseModel):
    post_id:int
    dir: int



class PostOut(BaseModel):
    Post: Post
    votes: int

    model_config = ConfigDict(from_attributes=True)


# For creating posts (input schema)

# # Upto here, this handles the direction of the user sending data to us. This is used when a client sssends data to you (e.g., when creating a new post)


# # US TO USER
# # For returning posts (output schema)
# class Post(PostBase):
#     id:int
   
#     created_at: datetime

#     class Config: 
#         orm_mode = True
    

    
# Postresponse because it represents a response

# So this model is what your FastAPI endpoint returns after interacting with the database.

# ORM=TRUE is important as it tells
# orm_mode = True
# he Problem

# Suppose your endpoint returns a SQLAlchemy object:

# post = db.query(models.Post).first()

# return post

# The object returned is not a dictionary.

# It's a SQLAlchemy object:

# <Post object at 0x123456>

# with attributes:

# post.id
# post.title
# post.content
# post.created_at
# Without orm_mode = True

# FastAPI expects a dictionary-like object.

# So when it sees:

# response_model=schemas.Post

# and you return:

# return post

# it gets confused and may raise validation errors.

# Because Pydantic expects:

# {
#     "id": 1,
#     "title": "My Post",
#     "content": "Hello",
#     "created_at": "2025-01-01"
# }

# but receives:

# <Post object>

# instead.

# Pydantic is told:

# "This object may come from SQLAlchemy. Read its attributes."

# So Pydantic does:

# post.id
# post.title
# post.content
# post.created_at

# and automatically converts them into:

# {
#   "id": 1,
#   "title": "My Post",
#   "content": "Hello",
#   "created_at": "2025-01-01T10:00:00"
# } 