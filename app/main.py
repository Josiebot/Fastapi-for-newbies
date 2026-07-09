
from fastapi import FastAPI
# Response, status, HTTPException, Depends
# from fastapi.params import Body
# # from pydantic import BaseModel
# from typing import Optional, List
# from random import randrange

# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
# from sqlalchemy.orm import Session


# @app.get("/")
# async def root():
#     return {"message": "Hello Jossy, welcome back to this class"}
# from . import models
# from .database import engine
from .routers import post, user, auth, vote
from .config import settings


from fastapi.middleware.cors import CORSMiddleware




# print(settings.database_password)
print("Username:", settings.database_username)
# print("Password:", settings.database_password)


# if __name__ == "__main__":
#     models.Base.metadata.create_all(bind=engine)
    
# models.Base.metadata.create_all(bind=engine)
app = FastAPI() # creates your API application instance.


# origins = ["https://www.google.com", "https://www.youtube.com"]
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "Hello Jossy, welcome back to this class"}


# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     # rating: Optional[int] = None


# while True:

#     try: 
#         conn = psycopg2.connect(host ='localhost', database = 'fastapi', user = 'postgres', password = 'postgres123', cursor_factory= RealDictCursor)

#         cursor = conn.cursor()
#         print("Succeful database connection")
        
#         break
    
#     except Exception as error:
#         print("Failed to connect to database")
#         print("Error was: ", error)
#         time.sleep(5)




# class UpdatePost(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None


# my_posts = [{"title": "title of post1", "content": "content of post 1", "id": 1},
#             {"title": "favorite foods", "content": "I like Tofu", "id": 2},
#             {"classes": "javascript", "lessons":"Lesson 1 to 5", "id": 5}] 



# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p
        
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
        
        # "Go through every item in my_posts. For each item, give me:

# i = the index (position)
# p = the post at that position"
# @app.get("/posts")
# def retrievedposts():
#     return{"Data": my_posts}
# //////////////////////////////////////////////    
