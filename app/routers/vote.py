from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags = ["Vote"]
)

@router.post("/", status_code = status.HTTP_201_CREATED)
def vote(vote:schemas.Vote, db:Session = Depends (database.get_db), current_user:int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()

    # This tells sql, query the posts table and "Only consider the row whose id equals the post_id sent by the user.

    if not post:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with id {vote.post_id} not found"
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



# select * posts LEFT JOIN users ON posts.user_id = users.id; 
# meaning "Return every post, and attach the matching user information where posts.user_id equals users.id - Means posts made by the same person
# LEFT JOIN users means Join (combine) the users table with posts. ON posts.user_id = users.id; means Match each post to the user who owns it.

# select posts.* from posts LEFT JOIN users ON posts.user_id = users.id;

# "Join the posts and users tables, but return only the columns from the posts table."
        # posts.* means all columns from the posts table only (id, title, content, user_id, etc.).
        # The LEFT JOIN is still used to match each post with its user, but no columns from users are included in the result.

# /////////SELECT
#     posts.id AS post_id,
#     posts.user_id,
#     users.id AS owner_id,
#     users.email
# FROM posts
# LEFT JOIN users
# ON posts.user_id = users.id;

# //////////////////////////////////////////////////////////////////////////////////////////
# select posts.*, count (votes.posts_id) from posts LEFT JOIN votes on posts.id = votes.posts_id group by posts.id
# You wrote:

# SELECT posts.id, COUNT(*)
# FROM posts
# LEFT JOIN votes
# ON posts_id = votes.users_id
# GROUP BY posts.id;

# and

# SELECT posts.id, COUNT(votes.posts_id)
# FROM posts
# LEFT JOIN votes
# ON posts_id = votes.users_id
# GROUP BY posts.id;

# The problem is:

# posts_id = votes.users_id

# This compares a post ID to a user ID, which are unrelated.

# The correct join is:
# SELECT posts.id, COUNT(votes.posts_id)
# FROM posts
# LEFT JOIN votes
# ON posts.id = votes.posts_id
# GROUP BY posts.id;

# Read it as:

# "Give me every post. For each post, attach all votes whose posts_id matches the post's id. Then count how many votes each post has."

# Why COUNT(votes.posts_id) instead of COUNT(*)?

# Suppose you have:

# posts
# id
# 1
# 2
# 3
# votes
# users_id	posts_id
# 5	1
# 6	1
# 8	2

# The query returns:

# post.id	COUNT(votes.posts_id)
# 1	2
# 2	1
# 3	0

# Notice that Post 3 still appears, even though it has no votes. That's because of the LEFT JOIN.

# If you had used COUNT(*), the result for Post 3 would be 1, because the LEFT JOIN still produces one row with NULL values for the votes columns. COUNT(*) counts that row, whereas COUNT(votes.posts_id) only counts non-NULL values.

# For counting votes, the standard query is:

# SELECT posts.id, COUNT(votes.posts_id) AS votes
# FROM posts
# LEFT JOIN votes
# ON posts.id = votes.posts_id
# GROUP BY posts.id;

# This is the pattern you'll commonly see in FastAPI and PostgreSQL tutorials when returning each post together with its vote count.

# What does this mean? select posts.*, count (votes.posts_id) from posts LEFT JOIN votes on posts.id = votes.posts_id group by posts.id

# This is one of the most useful SQL queries you'll use in a FastAPI project. Let's read it from left to right.

# SELECT posts.*, COUNT(votes.posts_id)
# FROM posts
# LEFT JOIN votes
# ON posts.id = votes.posts_id
# GROUP BY posts.id;
# SELECT posts.*

# Means:

# "Return every column from the posts table."

# If posts contains:

# id	title	content	user_id

# then posts.* returns all of them.

# COUNT(votes.posts_id)

# Means:

# "Count how many votes belong to each post."

# It counts only non-NULL values in votes.posts_id.

# FROM posts

# Start with the posts table.

# LEFT JOIN votes

# Means:

# "Include every post, even if it has no votes."

# ON posts.id = votes.posts_id

# Means:

# "Match each post with the votes whose posts_id equals that post's id."

# For example:

# posts
# ---------------------
# id   title
# 1    SQL
# 2    FastAPI
# 3    Django

# votes
# ---------------------
# users_id   posts_id
# 5          1
# 8          1
# 9          2

# The join produces:

# Post	Vote
# SQL	Vote by user 5
# SQL	Vote by user 8
# FastAPI	Vote by user 9
# Django	NULL

# Notice Django still appears because of the LEFT JOIN.

# GROUP BY posts.id

# This tells PostgreSQL:

# "Group together all rows that belong to the same post before counting the votes."

# So the final result becomes:

# id	title	content	user_id	count
# 1	SQL	...	4	2
# 2	FastAPI	...	7	1
# 3	Django	...	5	0
# In plain English

# The entire query means:

# "Show every post with all of its details, and next to each post show how many votes it has. Include posts that have never been voted on."

# /////////////////////////////
# select posts.*, count (votes.posts_id) as votesbyusers from posts LEFT JOIN votes on posts.id = votes.posts_id group by posts.id

# INDIVIDUAL POSTS
# select posts.*, count (votes.posts_id) as votesbyusers from posts LEFT JOIN votes on posts.id = votes.posts_id WHERE posts.id = 14 group by posts.id