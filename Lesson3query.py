
# from fastapi import FastAPI, Response, status, HTTPException, Depends
# from fastapi.params import Body
# from pydantic import BaseModel
# from typing import Optional
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
# from sqlalchemy.orm import Session
# from . import models
# from .database import engine, get_db


# models.Base.metadata.create_all(bind=engine)
# app = FastAPI() # creates your API application instance.


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



# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends (get_db)):
    
#    post =  db.query (models.Post).all()
#    return{"data":post}
# # //////////////////////////////////////////////    

# @app.get("/posts")
# def get_posts(db: Session = Depends (get_db)):
    
#     posts = db.query (models.Post).all()
#     print(posts)
#     return{"data": posts }

# # ///////////////CREATE APOST USING ORM///////////////

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def createpost(newpost:Post, db:Session = Depends(get_db)):
      
#     # cursor.execute ("""INSERT INTO nposts (title, content, published) values(%s,%s,%s) RETURNING *""",
#     #                  (newpost.title, newpost.content, newpost.published))
#     # created_post = models.Post(title=newpost.title, content=newpost.content, published=newpost.published)
# # Instead of this long appraoach, we use the ** model.
# #    print(newpost.dict())
#     created_post = models.Post(**newpost.dict())
#     db.add(created_post)
#     db.commit()
#     db.refresh(created_post)
#     return{"data":created_post}

# # ///////////////////////////////////
# @app.get("/posts/{id}", status_code=status.HTTP_200_OK)
# def get_post(id:int, db:Session = Depends(get_db)):
#     test_post = db.query(models.Post).filter(models.Post.id == id).first()

#     print(test_post)

#     if not test_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
   
#     return{"post_detail": test_post}


# # DELETE POST
# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int, db:Session = Depends(get_db)):
#   post = db.query(models.Post).filter(models.Post.id == id)

#   if post.first()== None:
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#   post.delete (synchronize_session=False)
#   db.commit()
#   return Response (status_code=status.HTTP_204_NO_CONTENT)
# # ///////////////////////////////////////////

# # UPDATE POST
# @app.put("/posts/{id}", status_code=status.HTTP_200_OK)
# def update_post(id:int, post:Post,db:Session = Depends(get_db) ):
    
#     post_query = db.query(models.Post).filter(models.Post.id == id)

#     updated_post = post_query.first()
                   
#     if updated_post == None:
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#     post_query.update ({'title': 'California', 'content': 'this is my updated content by Jossy_Julius'}, synchronize_session= False)
    
#     db.commit()
    
#     # return {"data": 'updated_post'}
#     return{"data": post_query.all()}



# # SQLalchemy does not know how to talk to database. It needs a driver, which is psycopg2