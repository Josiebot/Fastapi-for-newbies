from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'login')

#Secret_key
#expirationtime
#algorithm

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
 
def create_access_token(data:dict): 
    to_encode = data.copy()

    # Data:dict tells python I expect the data to be a dictionary
    

    expire = datetime.utcnow()+timedelta (minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    # We create a copy because It creates a copy we're about to add more information to it, and we don't want to accidentally change the original data.

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token:str, credentials_exception):
    try:
     
    
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]
                            )
        id:str = payload.get("user_id")
        
        if id is None:
            raise credentials_exception
        token_data =schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data
    
# Create token → Send token → Verify token → Identify user

# This is how FastAPI knows:

# "This request is coming from user #5."

def get_current_user(token: str = Depends (oauth2_scheme), db: Session = Depends (database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "could not validate credentials",headers = {"WWW-Authenticate":"Bearer"})
    
    token = verify_access_token (token, credentials_exception)

    user = db.query(models.User).filter (models.User.id == token.id).first()

    return user

    # return verify_access_token(token, credentials_exception)


# WHAT PART I ACTUALLY MEANS 
# Suppose the user logs in and you call:

# access_token = create_access_token(
#     data={"user_id": 14, "email": "ka9@gmail.com"}
# )
# 1. What does data: dict mean?
# def create_access_token(data: dict):

# dict means dictionary.

# It tells Python:

# "I expect data to be a dictionary."

# Example:

# data = {
#     "user_id": 14,
#     "email": "ka9@gmail.com"
# }

# The : dict is only a type hint for humans and VS Code.

# 2. Why data.copy()?
# to_encode = data.copy()

# Before:

# data = {
#     "user_id": 14,
#     "email": "ka9@gmail.com"
# }

# After:

# to_encode = {
#     "user_id": 14,
#     "email": "ka9@gmail.com"
# }

# It creates a copy.

# Why?

# Because we're about to add more information to it, and we don't want to accidentally change the original data.

# Think:

# Original dictionary
#         ↓
# Make a copy
#         ↓
# Modify the copy
# 3. What does this do?
# expire = datetime.now() + timedelta(
#     minutes=ACCESS_TOKEN_EXPIRE_MINUTES
# )

# Suppose current time is:

# 8:00 PM

# and:

# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Then:

# expire

# becomes:

# 8:30 PM

# This is the token's expiration time.

# 4. Why to_encode.update()?
# to_encode.update({"exp": expire})

# Before:

# {
#     "user_id": 14,
#     "email": "ka9@gmail.com"
# }

# After:

# {
#     "user_id": 14,
#     "email": "ka9@gmail.com",
#     "exp": "8:30 PM"
# }

# update() means:

# "Add new information to this dictionary."

# In JWT, "exp" is a standard field meaning:

# Expiration Time
# 5. What does jwt.encode() mean?
# encoded_jwt = jwt.encode(
#     to_encode,
#     SECRET_KEY,
#     algorithm=ALGORITHM
# )

# Before encoding:

# {
#     "user_id": 14,
#     "email": "ka9@gmail.com",
#     "exp": "8:30 PM"
# }

# After encoding:

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# This converts the dictionary into a JWT token.

# Think of it as:

# Dictionary
#     ↓
# Package it
#     ↓
# Digitally sign it
#     ↓
# JWT Token

# The SECRET_KEY is used to sign the token so nobody can change it.

# 6. Return the token
# return encoded_jwt

# Returns:

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# back to your login route.

# Then your login route returns:

# {
#   "access_token": "eyJhbGciOiJIUzI1NiIs...",
#   "token_type": "bearer"
# }
# The whole function in plain English
# Take user information
#         ↓
# Make a copy
#         ↓
# Add expiration time
#         ↓
# Convert to JWT token
#         ↓
# Sign it using SECRET_KEY
#         ↓
# Return the token

# That's all create_access_token() does. It takes user data (user_id, email, etc.), adds an expiry date, and turns it into a secure JWT string.


# GET_CURRENT_USER MEANS
# Who is the user making this request?"

