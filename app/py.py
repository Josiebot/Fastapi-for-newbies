
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
# from httpx import post
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2. extras import RealDictCursor
import time

# ///////////////////////////////
from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import Depends
from .database import engine, get_db


#
models.Base.metadata.create_all(bind=engine)


# (odels.Base.metadata.create_all(bind=engine)
# import psycopg2.extras means using the database connection engine, go through all models that inherit from models.Base, and create their tables in the database if they don’t already exist.”)

app = FastAPI() # creates your API application instance.


# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     # rating: Optional[int] = None

# Connect to database
# max_retries = 5
# attempts = 0

# while attempts < max_retries:
#     try:
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user ='postgres', password ='NewStrongPassword123!', cursor_factory=RealDictCursor)
        cursor = conn.cursor()  #To execute SQL statements
        print("Database connection was successful!")
        break
        # SQLALCHEMY_DATABASE_URL = "postgresql://postgres:@caltim3D@localhost:5432/fastapi"
# If we are not able to connect to it
    except Exception as error: #error stored in a variable called error
        print("connecting to database failed")
        print("error: ", error)
        time.sleep(2)

# if attempts == max_retries:
    # raise Exception("Could not connect to the database after several retries.")
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like TofuV ", "id": 2}] 

@app.get("/") # decorator
def root():
    return "Hello World"

@app.get ("/sqlalchemy")
def test_post(db:Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return{posts }


@app.get("/posts", response_model=list[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


# Create new post


# @app.get("/posts")
# def get_posts(db:Session = Depends(get_db)):
#     new_post = db.query(models.Post).all()
#     print(new_post) 
#     return new_post

# # CREATING A NEW POST


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# def create_posts(post: schemas.PostCreate, db:Session = Depends(get_db)):
# def create_posts(post:Post, db:Session = Depends(get_db)):
def create_posts(post:schemas.Post, db:Session = Depends(get_db)):
    
    # newpost = models.Post(title=post.title, content=post.content, published=post.published)
    newpost=models.Post (**post.dict())
    db.add(newpost)
    db.commit()
    db.refresh(newpost)
    return newpost


# ////////////////////////////////////////////////
# 4. RETRIEVE A POST
@app.get("/posts/{id}", response_model=schemas.Post)
def get_post(id: int, db:Session = Depends(get_db)):
    paypost = db.query(models.Post).filter(models.Post.id == id).all()

    if not paypost:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
  
    print(paypost)
   
    return {"post_detail":paypost }


#DELETING A POST
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id:int, db:Session = Depends(get_db)):
    new_post = db.query(models.Post).filter(models.Post.id == id)
    
    if new_post.first() == None:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} not found")

    print(new_post)
    new_post.delete(synchronize_session=False)
    db.commit()

    return{"details":new_post}

# # UPDATING A POST
@app.put("/posts/{id}", response_model=schemas.Post)
# def update_posts(id: int, updated_post:Post, db:Session = Depends(get_db)): 
def update_posts(id: int, updated_post:schemas.PostCreate, db:Session = Depends(get_db)): 
# def update_posts(id: int, updated_post:Post, db:Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} does not exist")
    
    # post_query.update({'title':'updated title', 'content': 'updated content'}, synchronize_session=False)

    post_query.update(updated_post.dict(), synchronize_session=False) 
    # updated_post.dict() → turns the Pydantic model into a dictionary.
    db.commit()
    print(post)
    return {"data": post_query.first()}