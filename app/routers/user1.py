
# from .. import models, utils, schemas

# from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
# from fastapi.params import Body
# from .. database import engine, get_db
# from sqlalchemy.orm import Session
 
# router = APIRouter(
#     prefix = "/users",
#     # /posts/{id} becomes /id
#     tags = ['users']
# )

# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def createuser(user:schemas.UserCreate, db:Session = Depends(get_db)):
      
#     #hash the ppassword = user.password
#     # hashed_password = pwd_context.hash(user.password)
#     # # user.password = hashed_password'

#     # in utils this looks like this - 
# # def hash (password:str):
# #     return pwd_context.hash(password)

#     hashed_password = utils.hash(user.password)
#     # hashed_password = pwd_context.hash(user.password)
#     user.password = hashed_password
   
#     newuser = models.User(**user.dict())
#     db.add(newuser)
#     db.commit()
#     db.refresh(newuser)
#     return newuser


# # SQLalchemy does not know how to talk to database. It needs a driver, which is psycopg2
# @router.get('/{id}', response_model = schemas.UserOut)
# def get_user(id:int, db:Session = Depends(get_db)):
#     user = db.query (models.User).filter(models.User.id ==id).first()
    

#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} not found")

#     else:
#         return user
