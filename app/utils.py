from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
# This command creates a tool that knows how to:

# Hash passwords
# Verify passwords
# Use bcrypt as the hashing algorithm

# hashed_password = pwd_context.hash(user.password)
# user.password = hashed_password

def hash (password:str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#  verify() checks whether the user's entered password
# matches the hashed password stored in the database. This verifies the password by comparing it with the hashed password