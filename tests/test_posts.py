from http import client
from typing import List

import pytest
from app import schemas

def test_get_all_posts(authorized_client,test_posts ):
    res = authorized_client.get("/posts")

    def validate (post):
        return schemas.PostOut(**post)

    posts_map = map(validate, res.json())
    print(list(posts_map))
    print("...............")

    assert res.json()
    assert res.status_code == 200
    assert len(res.json()) == len(test_posts)
    print(res.json())
    print("////////////")





def test_get_all_posts(authorized_client,test_posts ):
    res = authorized_client.get("/posts")
    assert res.json()
    assert res.status_code == 200
    assert len(res.json()) == len(test_posts)
    print(res.json())
    print("////////////")

def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get ("/posts")
    assert res.status_code == 401

def test_unauthorized_user_get_one_posts(client, test_posts):
    newpost = test_posts[0]
    res = client.get (f"/posts/{newpost.id}")
    # res = client.get ("/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get("/posts/097")
    assert res.status_code == 404


def test_get_one_post(authorized_client, test_posts):
    posts = test_posts[0]
    res = authorized_client.get(f"posts/{posts.id}")
    print(res.json())
    assert res.status_code == 200
    post = schemas.PostOut(**res.json())
    print(post)
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content
    assert post.Post. title == test_posts[0].title


# CREATING A POST
@pytest.mark.parametrize("title, content, published",[
    ("awesome new title", "awesome new content", True), 
    ("favorite pizza", "i love pepperon", False), 
    ("Awesome Jossy", "awesome new life", True)
])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    res = authorized_client.post("/posts", json = {"title": title, "content":content, "published":published})
    created_post = schemas.Post(**res.json())

    # Before running this test, give me these object - test_create_post(authorized_client, test_user, test_posts

    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.user_id == test_user['id']
# "What happens when an authenticated user requests a post that doesn't exist?"

def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    res = authorized_client.post("/posts", json = {"title": "arbitrary title", "content":"content"})
    created_post = schemas.Post(**res.json())

    assert res.status_code == 201
    assert created_post.title == "arbitrary title"
    assert created_post.content == "content"
    assert created_post.published == True
    assert created_post.user_id == test_user['id']


def test_unauthorized_user_create_post(client, test_user, test_posts):
    res = client.post("/posts", json = {"title": "arbitrary title", "content":"content"})
    assert res.status_code == 401

def test_unauthorized_user_delete_post(client, test_user, test_posts):
    res =client.delete("/posts/{test_posts[0].id}")
    assert res.status_code == 401


# VALID DELETIONsuccessfully


def test_delete_post_success (authorized_client, test_user, test_posts):
    res = authorized_client.delete("/posts/{test_posts[0].id}")
    assert res.status_code == 422
# posts = [schemas.Post.model_validate(post) for post in res.json()]
# assert len(posts) == len(test_posts)

def test_delete_post_non_exist(authorized_client, test_user, test_posts):
    res = authorized_client.delete("/posts/097}")
    assert res.status_code == 422

# USER DELETING A POST OWNED BY ANOTHR UserWarning
def test_delete_other_user_posts (authorized_client, test_user, test_posts):
    res = authorized_client.delete("/posts/{test_posts[3].id}")
    assert res.status_code == 422

# UPDATE POSTS///
def test_update_post(authorized_client, test_user, test_posts):
    data = {
        "title":"updated title", "content":"updated content", "id":"test_posts[0].id", "published": True
    }
    res = authorized_client.put(f"/posts/{test_posts[0].id}", json = data)
    updated_post = schemas.Post(**res.json())
    assert res.status_code == 200
    assert updated_post.title ==data['title']
    assert updated_post.content ==data['content']
    assert updated_post.published ==data['published']
    print("test_posts[0]")


def update_other_user_post(authorized_client, test_user, test2_user, test_posts):
    data = {"title": "updated title",
            "content": "updated content", "id": test_posts[3].id}
    res = authorized_client.put(f"/posts/{test_posts[3].id}", json = data)
    assert res.status_code == 401


def test_unauthorized_user_update_post(client ):
    res = client.put("posts/098")
    assert res.status_code == 401

def test_update_post_non_exist(authorized_client, test_user, test_posts):
    data = {
    "title": "Updated",
    "content": "Updated content",
    "published": True
}
    res = authorized_client.put("/posts/097}", json = data)
    assert res.status_code == 422
    # What happens when a logged-in user tries to update a post that doesn't exist?"