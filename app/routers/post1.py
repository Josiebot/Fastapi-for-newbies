

# from .. import models, utils, schemas, oauth2

# from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
# from fastapi.params import Body
# from .. database import engine, get_db
# from sqlalchemy.orm import Session

# from typing import List

# router = APIRouter(
#     prefix = "/posts",
#     # /posts/{id} becomes /id
#     tags= ['posts']
# )


# @router.get("/", response_model=List[schemas.Post])
# def get_posts(db: Session = Depends (get_db), current_user:int = Depends(oauth2.get_current_user)):
# # @router.get("/", response_model=List[schemas.Post])
# # def get_posts(db: Session = Depends (get_db)):
    
#     posts = db.query (models.Post).all()
#     print(posts)
#     return posts

# # ///////////////CREATE APOST USING ORM///////////////

# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# def createpost(newpost:schemas.PostCreate, db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
# # def createpost(newpost:schemas.PostCreate, db:Session = Depends(get_db), get_current_user:int = Depends(oauth2.get_current_user)):
#     print(current_user.email)
#     created_post = models.Post(**newpost.dict())
#     db.add(created_post)
#     db.commit()
#     db.refresh(created_post)
#     return created_post

# # ///////////////////////////////////
# @router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Post)
# def get_post(id:int, db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
# # def get_post(id:int, db:Session = Depends(get_db)):
#     test_post = db.query(models.Post).filter(models.Post.id == id).first()

#     print(test_post)

#     if not test_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
   
#     return test_post


# # DELETE POST
# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int, db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
# # def delete_post(id:int, db:Session = Depends(get_db)):
#   post = db.query(models.Post).filter(models.Post.id == id)

#   if post.first()== None:
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#   post.delete (synchronize_session=False)
#   db.commit()
#   return Response (status_code=status.HTTP_204_NO_CONTENT)
# # ///////////////////////////////////////////

# # UPDATE POST
# @router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Post)
# def update_post(id:int, post:schemas.PostCreate,db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
# # def update_post(id:int, post:schemas.PostCreate,db:Session = Depends(get_db) ):
    
#     post_query = db.query(models.Post).filter(models.Post.id == id)

#     updated_post = post_query.first()
                   
#     if updated_post == None:
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#     post_query.update ({'title':'California city new', 'content': 'this is my updated content by Jossy_Julius'}, synchronize_session= False)
    
#     db.commit()
    
#     return {"data": 'updated_post'}
#     return post_query.first()

