# from fastapi import FastAPI
# from fastapi.params import Body
# from pydantic import BaseModel
# from typing import Optional
# from pprint import pprint


# app = FastAPI()

# class Post (BaseModel):  
#     title:str
#     content:str
#     published:bool = True  # Optional field with a default value
#     rating: Optional[int] = None

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]
# @app.get("/")
# async def root():
#     return{"message": "Its Jossy again!❤️🎉. Welcome to my API"}


# @app.get("/socialposts")
# def get_posts():
#     return {"message": "These are my social media posts👌"}

# @app.post("/createposts")
# def create_posts(newpost: Post):
# # def create_posts(newpost: dict = Body(...)):
#     print(newpost)
#     print(newpost.title) 
#     print(newpost.rating) 
#     # return{"message": f"title: {newpost['title']}\n             scontent: {newpost['content']}"}
#     return{"data": newpost} 
