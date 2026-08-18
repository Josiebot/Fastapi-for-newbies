
# from fastapi import FastAPI, Response, status, HTTPException
# from fastapi.params import Body
# from pydantic import BaseModel
# from typing import Optional
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time


# app = FastAPI() # creates your API application instance.

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None



# while True:

#     try:   
#         conn = psycopg2.connect(host ='localhost', database = 'postgres', user = 'postgres', password = 'postgres123', cursor_factory= RealDictCursor)

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
        
#         # "Go through every item in my_posts. For each item, give me:

# # i = the index (position)
# # p = the post at that position"
    


# @app.get("/posts")
# def get_posts():
#     cursor.execute("""SELECT * from nposts """)
#     posts = cursor.fetchall()
#     print(posts)
#     return{"data": posts }


# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def createpost(newpost:Post):
#     # print(newpost.rating)
#     # print(newpost.dict())
#     cursor.execute ("""INSERT INTO nposts (title, content, published) values(%s,%s,%s) RETURNING *""",
#                      (newpost.title, newpost.content, newpost.published))
#     created_post = cursor.fetchone()
#     conn.commit()
    
    
#     return{"data":created_post}


# @app.get("/posts/{id}", status_code=status.HTTP_200_OK)
# def get_post(id:int, response: Response):
#     cursor.execute("""SELECT * FROM nposts where id = %s""", (str(id),))
#     test_post = cursor.fetchone()


  
#     # return{"post_detail": f"Here is the post id {id}"}
    
#     if not test_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return{"message": f"post with id{id} was not found"}
#     return{"post_detail": test_post}

# # DELETE POST
# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int):
#   cursor.execute (""" DELETE from nposts where id = %s returning *
#                     """, (str(id),))
#   deletedpost = cursor.fetchone()
#   conn.commit()
#   if deletedpost == None:
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#   return Response (status_code=status.HTTP_204_NO_CONTENT)


# # UPDATE POST
# @app.put("/posts/{id}", status_code=status.HTTP_200_OK)
# def update_post(id:int, post:Post):
#     cursor.execute ("""UPDATE nposts SET title = %s, content = %s, published = %s  where id = %s RETURNING *
#                     """, (post.title, post.content, post.published, str(id)))
                   
#     updated_post = cursor.fetchone()
#     conn.commit()


#     if updated_post == None:
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
   
   
#     return {"data": updated_post}
