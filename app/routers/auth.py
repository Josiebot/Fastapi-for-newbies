from fastapi import APIRouter, Depends, status, HTTPException
# Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags = ['Authentication'])
 
@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends (), db: Session = Depends(database.get_db)):


    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException (status_code=status.HTTP_403_FORBIDDEN, detail = "invalid credentials")
    
    if not utils.verify (user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "Invalid credentials")

# create token

    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    
# return token
    return {"access_token" : access_token, "token_type": "bearer"}

# def login(user_credentials: schemas.UserLogin,
#           db: Session = Depends(database.get_db)):
# This basically means, When someone calls /login, FastAPI should extract the OAuth2 login form into an OAuth2PasswordRequestForm object called user_credentials, obtain a database session using database.get_db(), and pass both into the login() function."

# username
# password
# def login(user_credentials: schemas.UserLogin, db: Session = Depends(database.get_db)):

    
    # user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    # {"username": "xxx",
    #  "password":"ÿyyy"
    #  } when you retrieve the users attempt credentials, they will be stored in a field called username and not email as earlier

# def login(user_credentials: schemas.UserLogin,
# #           db: Session = Depends(database.get_db)):
    # user=db.query(models.User).filter(models.User.email == User.credentials.email).first()
    # This is for login that's why we are checkin the email.
    
    # if not user:
        # raise HTTPException (status_code=status.HTTP_403_FORBIDDEN, detail = "invalid credentials")

    #  if not utils.verify (user_credentials.password, user.password):
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "Invalid credentials")
    # Here we are comparing the user password with the logging in password

    # user_credentials: OAuth2PasswordRequestForm = Depends()
    # 
    # FastAPI, I expect the login credentials to come in the OAuth2 form format. Please read the request, create an OAuth2PasswordRequestForm object from it, and give it to me as user_credentials."