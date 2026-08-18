
# from fastapi import FastAPI, Response, status, HTTPException
# from fastapi.params import Body
# # from httpx import post
# from pydantic import BaseModel
# from typing import Optional
# from random import randrange


# app = FastAPI() # creates your API application instance.

# # request Get method url: "/"

# # CRUD APPLICATION 
# # Every application must be able to create (post), read (get), update (put/patch), and delete (crud)

# # Update the create post path operation so that we can retrieve the title and the content from our front end and create a brand new post and store it within our my_posts array


# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None


# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#             {"title": "favorite foods", "content": "I like Tofu", "id": 2}] 


# #1. GET ALL POSTS
# @app.get("/posts")
# def get_posts():
#     return {"data": my_posts}

# # CRUD
# # CREATE - /@app.post("/posts") (Posts requests)
# # Creates a new post with the data provided in the request body. post request whenever creating an entity.

# # READ - /@app.get("/posts/{id}")
# #    @app.get("/posts") - Retrieves all posts/data - send a get request to /posts
# # /@app.get("/posts/{id}") - When getting detailed information about an individual post, we send a get request to /post/{id}

# # UPDATE - /@app.put("/posts/{id}")
# # Entails updating a preexisting post. We use put, we pass all the information for updating it. With put, you have to provide all the same information so that we can uodate the entity in the backend
# # With patch, we pass the specific idea we want to change. with patch, you send the specific info only. 
# # DELETE - /@app.delete("/posts/{id}")

# # 
# # 2. CREATE A POST

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(payPost: Post):
#     print(payPost)
#     print(payPost.dict()) 
#     payPost_dict = payPost.dict()
#     # # post.dict() = turn the validated Pydantic object into a normal dictionary so you can modify it, like adding an "id". Makes a mutable dictionary copy. # Why? Because the Pydantic model is immutable (safer), but you may need to modify the data (like adding an id).
#     payPost_dict["id"] = randrange(0, 100000)
#     my_posts.append(payPost_dict)
#     # # # my_posts.append(post_dict)
#     return {"data": payPost_dict}
# # The argument post: Post means FastAPI will expect the request body to match a Pydantic model called Post. def create_posts(post: Post): 👉 means this function takes a request body, validates it against the Post model, and makes it available as the variable post.# So post is a Pydantic model object containing the client’s data. ✅
# # print(post) → would print the Pydantic model object.

# # print(post.dict()) → would print it as a normal Python dictionary.
# # Converts the validated Pydantic object (post) into a regular Python dictionary (post_dict). post_dict = post.dict()

# # Example: if you sent {"title": "My Post", "content": "Hello"}, then post_dict will be:
# # randrange(0, 100000) generates a random number between 0 and 100,000 (like a fake database ID).
# # Appends this new dictionary (the new post) to the my_posts list.

# # my_posts is acting like your temporary in-memory database (instead of using PostgreSQL/MySQL).
# # return {"data": post_dict"} Sends back a response to the client.


# # //////////////////////////////////////////////////
# # 3. FINDING/GETTING INDIVIDUAL POSTS
# def find_post(id: int):
#     for p in my_posts:
#         print("currently checking:", p)
#         if p["id"] == id:
#             return p
#     return None
# print(find_post(2))

# # print(p) I want to print the post that is found.
# # print(p.dict())  # This will raise an error    so what do I do here? 

# # Because find_post(2) returns a dictionary (the post), not a Pydantic model. Dictionaries don’t have a .dict() method.
# # Great. Now I want to search for the IDs in postman, id 1 and 2 from my_posts. 

# # ////////////////////////////////////////////////
# # 4. RETRIEVE A POST
# @app.get("/posts/{id}")
# def get_post(id: int):
#     post = find_post(id) #“Take the id from the request, call the helper function find_post, and store whatever it finds in the variable post.”
#     print(id)
#     print(type(id))
#     return {"post_detail": post}
# # Great. I want to understand the part post=find_post(id). What is happening there?
# # The function find_post(id) is called with the provided id. It searches through the my_posts list to find a post with a matching id.
# # If a matching post is found, it is returned and assigned to the variable post.      


# # # This function searches through the my_posts list to find a post with a matching id.
# # for p in my_posts - "Go through every note (p) in the box one by one."
# # if p has an id, which is equals to id, return the post - For each note, check: "Does this note’s id number match the id number I was asked to find?"

# # ////////////////////////////////////////////////////
# # Retrieving post
# # {id} here represents a path parameter and it represents the unique identifier for a specific post.
# # @app.get("/posts/{id}")
# # def get_post(id: int):
# #     post = find_post(id)
# #     print(id)
# #     print(type(id))
# #     return {"post_detail": post}
# # # What if the post with the given ID does not exist? We should handle that case.

# # //////////////////////////////////////////////////
# # @app.get("/posts/latest")
# # def get_latest_post():
# #    posts=my_posts[len(my_posts)-2]
# #    print(posts)
# #    return {"post_detail": posts}
# # # # what happening in this case?
# # # # This endpoint ( /posts/latest endpoint) retrieves the latest post from the my_posts list and returns it in the response. 
# # # # which endpoint? - The /posts/latest endpoint.
# # (FastAPI doesn’t know "latest" is special — it just sees it as text after /posts/ and assumes it should go into {id} unless you define a more specific route first.)

# # @app.get("/posts/{id}")
# # def get_post(id: int, response: Response):
# #     print(id)
# #     print(type(id))

# #     post = find_post(id)
# #     if not post:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found")
# #         # response.status_code = 404
# #                 # response.status_code = status.HTTP_404_NOT_FOUND
# #         # return {"message": f"Post with id {id} was not found"}

# #         return {"post_detail": post}


# @app.get("/posts/{id}")
# def get_post(id:int):
#     post = find_post(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found")
#     return {"post_detail": post}



#     # return {"post_detail": post}
# # # Validation to ensure whatever data is passed called be converted tp an integer. The way its done above. 

# # # EXAMPLE
# # # If you want to get the post with ID 1, you would send a GET request to /posts/1
# # # If you want to create a new post, you would send a POST request to /posts with the post data in the body
# # # If you want to update the post with ID 1, you would send a PUT request to /posts/1 with the updated post data in the body




# # # 4. UPDATE A POST
# # # @app.put("/posts/{id}")
# # # def update_post(id: int, post: Post):
# # #     print(id)
# # #     print(type(id))

# #     existing_post = find_post(id)
# #     if not existing_post:
# #         return {"Error": "Post not found"}

# #     existing_post.update(post.dict())
# #     return {"data": existing_post}

# # # Telling the front end that the id you are looking for does not actually exist

# # /////////////////////////////////////////


# # 4. DELETE A POST

# def find_index_post(id: int):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
#     return None
# print(find_index_post(2))

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT) 
# # updating the status code to 204
# def delete_post(id:int):
#     # deleting post with the given id
#     # find the index in the array that has that id
#     # my_posts.pop(index) - remove that item
#     # return a response
#     index= find_index_post(id)
#     if index==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
#     my_posts.pop(index)
#     return {"message": f"Post with id {id} has been deleted"}
# # 5. UPDATE A POST


# @app.put("/posts/{id}")
# def update_post(id:int, post: Post):

#     index = find_index_post(id)
#     if index==None: 
#         # which index are you referring to here? The index of the post in the my_posts list that matches the given id. 
#         # fROM WHERE?
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
    
#     post_dict= post.dict()
#     # Grab post_dict from the fronend and convert it to a dictionary.
#     # which is the frontend in this case? The data sent in the request body when calling this endpoint.That is the data in represented by the post parameter of type Post.
#     # So post is a Pydantic model object containing the client’s data. ✅
#     post_dict["id"]=id
#     my_posts[index]= post_dict
#     # what is the meaning of this?my_posts[index]= post_dict
#     # This line updates the post at the found index in the my_posts list with the new data from post_dict.
#     print(post)
#     return {"Message": post_dict}

# # how do i create a new folder called app in the terminal?

# # mkdir app
# # And    how do i move main.py into that app folder?
# # inside that I want to add a new file called __init__.py
# # mv main.py app/.
# # Awesome. What does __init__.py do?
# # It tells Python that this directory should be treated as a package. It can be an empty file, but it can also execute initialization code for the package if needed.
# # Why would I want to do that? How do i add an __init__.py file in the terminal?
# # touch __init__.py

# # NOTE
# # When you run uvicorn, you don’t point to a file path (/ or .py), you point to a Python import path:

# # uvicorn package.module:variable