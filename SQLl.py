
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


# why am i getting an error here?
# pip install psycopg2-binary
#

# import psycopg2.extras
# import time

# (odels.Base.metadata.create_all(bind=engine)
# import psycopg2.extras means using the database connection engine, go through all models that inherit from models.Base, and create their tables in the database if they don’t already exist.”)

app = FastAPI() # creates your API application instance.


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

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
    return {"message": "Hello World"}
  

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM products  """)
    products = cursor.fetchall()
    
    return {"NEW data": products}

#1. GET ALL POSTS
# @app.get("/posts")
# def get_posts():
#     return {"data": my_posts}


# 2. CREATING A NEW POST

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    
    cursor.execute(""" INSERT INTO socialposts (content, title, published) VALUES (%s, %s, %s) RETURNING *""", 
                   (post.content,post.title, post.published))
   
    new_post = cursor.fetchone()
    conn.commit()
    print(new_post)
    return {"data":new_post}


# ////////////////////////////////////////////////
# 4. RETRIEVE A POST
@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute(""" SELECT * from socialposts where id = %s""", (str(id)))
    test_post = cursor.fetchone()
  
    print(test_post)
    print(type(id))
    return {"post_detail":test_post }


#DELETING A POST
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id = int):
    cursor.execute("""  DELETE FROM posts WHERE id = %s returning *""", (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()

if delete_posts == None:
    raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} not found")

    print(delete_posts)
    # return{"details":delete_posts}

# UPDATING A POST
@app.put("/posts/{id}")
def update_posts(id: int, post: Post):
    cursor.execute("""  UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published))

    updated_post = cursor.fetchone()
    conn.commit()
    

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} does not exist")
    print(updated_post)
    return {"data": updated_post}