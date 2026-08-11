

from .. import models, schemas, oauth2

from fastapi import Response, status, HTTPException, Depends, APIRouter
# from fastapi.params import Body
from .. database import  get_db
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional

from typing import List

router = APIRouter(
    prefix = "/posts",
    # /posts/{id} becomes /id
    tags= ['posts']
)


@router.get("/", response_model=List[schemas.PostOut])
# @router.get("/")
def get_posts(db: Session = Depends (get_db), current_user:models.User = Depends(oauth2.get_current_user),
              limit:int = 10, skip: int =0, search: Optional [str] =""):

    print("LIMIT =", limit)
   
# def get_posts(db: Session = Depends (get_db), current_user:int = Depends(oauth2.get_current_user)):
# @router.get("/", response_model=List[schemas.Post])
# def get_posts(db: Session = Depends (get_db)):
    
    # posts = db.query (models.Post).all()
    # posts = db.query(models.Post).limit(limit).offset(skip).all()
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    # adding space in URL  ({{URL}}posts?limit=5&search=MyDeborah%20season)

    # select posts.*, count (votes.posts_id) as votesbyusers from posts LEFT JOIN votes on posts.id = votes.posts_id WHERE posts.id = 9 group by posts.id
    results = db.query(models.Post, func.count(models.Vote.posts_id).label ("votes")).join(models.Vote, models.Vote.posts_id == models.Post.id, isouter=True). group_by (models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    print(results)
    
   
    print("POST COUNT =", len(posts))
    # posts = db.query (models.Post).filter(models.Post.user_id == current_user.id).all()

   
    print(current_user.id)
    return results

# ///////////////CREATE APOST USING ORM///////////////

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def createpost(newpost:schemas.PostCreate, db:Session = Depends(get_db), current_user:models.User = Depends(oauth2.get_current_user)):
# def createpost(newpost:schemas.PostCreate, db:Session = Depends(get_db), get_current_user:int = Depends(oauth2.get_current_user)):
    print(current_user.email)
    print(current_user.id)
    # created_post = models.Post(**newpost.dict())
    created_post = models.Post(
    user_id=current_user.id,
    **newpost.dict()
)
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return created_post


# ///////////////////////////////////
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.PostOut)
def get_post(id:int, db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
# def get_post(id:int, db:Session = Depends(get_db)):
    test_post = db.query(models.Post).filter(models.Post.id == id).first()

    print(test_post)

    # if test_post== 'cond is None':
    #     raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    # if test_post.user_id != current_user.id:
    #   raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "Not authorized to perform requested action jod")
    test_post = db.query(models.Post, func.count(models.Vote.posts_id).label ("votes")).join(models.Vote, models.Vote.posts_id == models.Post.id, isouter=True). group_by (models.Post.id).filter(models.Post.id == id).first()


    if not test_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
   
    return test_post


# DELETE POST
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db:Session = Depends(get_db), current_user:models.User = Depends(oauth2.get_current_user)):
# def delete_post(id:int, db:Session = Depends(get_db)):
#   post = db.query(models.Post).filter(models.Post.id == id)
# "current_user: models.User = Depends(oauth2.get_current_user) means: 'Automatically verify the JWT token, look up the matching user in the users table, and give me that User object as current_user.'
  post_query = db.query(models.Post).filter(models.Post.id == id)
  post = post_query.first()

  if post== 'cond is None':
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
  if post.user_id != current_user.id:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "Not authorized to perform requested action")

  post_query.delete (synchronize_session=False)
  db.commit()
  return Response (status_code=status.HTTP_204_NO_CONTENT)
# ///////////////////////////////////////////

# UPDATE POST
@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Post)
def update_post(id:int, post:schemas.PostCreate,db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
# def update_post(id:int, post:schemas.PostCreate,db:Session = Depends(get_db) ):
    
    post_query = db.query(models.Post).filter(models.Post.id == id)

    updated_post = post_query.first()
                   
    if updated_post == 'cond is None':
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    if updated_post.user_id != current_user.id:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "Not authorized to perform requested action")
    # post_query.update ({'title':'California city new', 'content': 'this is my updated content by Jossy_Julius'}, synchronize_session= False)
    post_query.update(
    post.dict(),
    synchronize_session=False
)
    
    db.commit()
    
    # return {"data": 'updated_post'}s
    return post_query.first()


# Current user:model.User

# Get the currently authenticated user and pass the User object into current_user."

# Breaking it down:

# current_user: models.User = Depends(oauth2.get_current_user)
# Depends(...) → Call get_current_user() automatically.
# oauth2.get_current_user → Verify the JWT, find the user in the database, and return that user.
# current_user → The variable that receives the returned user.
# : models.User → This variable is expected to be a SQLAlchemy User object.

# So when your route runs, it's as if FastAPI did this behind the scenes:

# current_user = get_current_user()

# and current_user contains something like:

# User(
#     id=5,
#     email="grace@gmail.com",
#     password="..."
# )

# That's why you can immediately use:

# current_user.id
# current_user.email

# A simple one-line summary to remember is:

# "Automatically retrieve the logged-in user and make them available as current_user."