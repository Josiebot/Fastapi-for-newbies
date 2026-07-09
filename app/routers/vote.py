from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags = ["Vote"]
)

@router.post("/", status_code = status.HTTP_201_CREATED)
def vote(vote:schemas.Vote, db:Session = Depends (database.get_db), current_user:int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(
    models.Post.id == vote.post_id).first()

    # This tells sql, query the posts table and "Only consider the row whose id equals the post_id sent by the user.

    if not post:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with {vote.post_id} not found"
    )

    vote_query = db.query(models.Vote).filter(models.Vote.posts_id == vote.post_id, models.Vote.users_id == current_user.id)


    found_vote = vote_query.first()

    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail = f"user {current_user.id} has already voted on post {vote.post_id}")
        # if we didn't find a vote we create a brand noew vote
        new_vote = models.Vote(posts_id = vote.post_id, users_id = current_user.id)

        db.add (new_vote)
        db.commit()
        return {"message": "successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail = "vote does not exist")
        
        vote_query.delete(synchronize_session=False)
        db.commit()

        return{"message":"successfully deleted vote"}



