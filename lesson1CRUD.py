
# from fastapi import FastAPI, Response, status, HTTPException
# from fastapi.params import Body
# from pydantic import BaseModel
# from typing import Optional
# from random import randrange

# app = FastAPI() # creates your API application instance.

# @app.get("/")
# async def root():
#     return {"message": "Hello Jossy, welcome back to this class"}

# # @app.get("/")
# # get. - METHOD"
# # ("/") - Path
# # async def root():
# #     return {"message": "Hello Jossy, welcome back to this class"}



# #  @app.get("/posts")
# # # def root():
# #     return{"message": "My Posts post"}


# # @app.post("/createposts")
# # def createpost(payload: dict = Body(...)):
# #     print(payload)
# #     return{"new_post": f"\ntitle{payload['title']} \ncontent: {payload['content']}"}


# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None


# class UpdatePost(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None


# my_posts = [{"title": "title of post1", "content": "content of post 1", "id": 1},
#             {"title": "favorite foods", "content": "I like Tofu", "id": 2},
#             {"classes": "javascript", "lessons":"Lesson 1 to 5", "id": 5}] 



# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p
        
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
        
#         # "Go through every item in my_posts. For each item, give me:

# # i = the index (position)
# # p = the post at that position"
    


# @app.get("/posts")
# def retrievedposts():
#     return{"Data": my_posts}


# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def createpost(newpost:Post):
#     # print(newpost.rating)
#     # print(newpost.dict())
#     post_dict = newpost.dict()
#     post_dict["id"] = randrange(0,10000)
#     my_posts.append(post_dict)
    
#     return{"data":post_dict }


# @app.get("/posts/{id}", status_code=status.HTTP_200_OK)
# def get_post(id:int, response: Response):
#     print(id)
#     # return{"post_detail": f"Here is the post id {id}"}
#     post = find_post(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return{"message": f"post with id{id} was not found"}
#     return{"post_detail": post}

# # DELETE POST
# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int):
#     index = find_index_post(id)
#     if index == None:
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#     my_posts.pop(index)
#     # return{"message": f"post with id {id} was successfully deleted"}
#     return Response (status_code=status.HTTP_204_NO_CONTENT)


# # UPDATE POST
# @app.put("/posts/{id}", status_code=status.HTTP_200_OK)
# def update_post(id:int, post:Post):
#     index = find_index_post(id)
#     if index == None:
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
#     post_dict = post.dict()
#     post_dict['id'] = id
#     my_posts[index] = post_dict
   
#     return {"data": post_dict}

# # "Find the post with this ID. If it doesn't exist, return a 404 error. If it does exist, take the new data the user sent, keep the same ID, replace the old post with the new one, and return the updated post."








# # ADDITIONAL NOTES

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
#     # return {"Message": Post_dict}



#     # MORE LESSONS
    
# # First, create a virtual environment
# # Make sure the environment is changed from the global interpreter to a specific one, mainlt python.exe
# #   To achieve this, view, command pallette, select interpreter, enter path (.\venv\Scripts\python.exe). Path begins at the root of the product directory
# # PATH TO Activate 
# #   Make sure the terminal is using the virtual environment by typing a path to the activate.exe
# # Next install pip install fastapi[all]. Mine works with py -m pip install fastapi[all]
# # Next, lets check what was installed with pip freeze
# # Below fastapi is the name of the library
# from fastapi import FastAPI 
# from fastapi.params import Body
# from pydantic import BaseModel
# from typing import Optional
# app = FastAPI() # creates your API application instance.

# # request Get method url: "/"

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None

#     # If the user doesn't provide us with a value, we can give a default value. If provided, whatever value is given goes
# # # Lets create an instance of API here
# # # Path Operation
# # @app.get("/") # this is a decorator that defines a route (an endpoint).
# # async def root():
# #     return{"message": "Hello Gitimo. Yoh!!"}

# # # @app.get("/") → this is a decorator that defines a route (an endpoint).

# # # "/" means the homepage (root path).

# # # get means it responds to HTTP GET requests.

# # # async def root(): → defines an asynchronous function to handle requests.

# # # return {"message": "Hello Gitimo"} → FastAPI automatically converts this Python dictionary into JSON, so the browser or client sees:

# # # Lets start our web server app
# # # We run the uvicorn m

# # @app.get("/posts")
# # def get_posts():
# #     return {"data": "This is your post Jossy!"}

# #     # Get and post - Think of GET like reading a book, and POST like writing in the book.
# #     # Get is often used for retrieving data
# #     # Get requests is for getting data from the API server while a post request is for sending data to the API server
# # # @app.post("/createposts") 
# # # # # Whatever specific URL the user should go to in order to create the posts
# # # def create_posts():
# # # #     print(pay)
# # #     return {"message": "Hi Jossy, successfully created post"}

# # # Not
# # # Anytime we send a request to a API server, it goes down the list of path operations to find the first match after which it stops running the code.

# # # SEND DATA TO THE API SERVER
# # # 1. USING A METHOD APPROACH
# # # The whole idea behind a post request is to send data to the API server (Body of the request)
# # @app.post("/createposts")
# # # def create_posts(new_post: Post):
# # def create_posts (payLoad: dict = Body(...)): 
# # #     #  This will extract the JSON body, convert it to a Python dict, and save in payload
   
# # #     # This will extract all the fields from the body and convcert it to python dictionary and store it into a variable called payload
# # #     print(new_post.title)
# # #     # return{"Message": "How are you?"}
# # #     # return {"New_post": f"title{payLoad['title']} \n content:{payLoad['content']}"}
# #     print(payLoad)              # shows Pydantic model 
# #     return {
# #         "title": payLoad["title"],
# #         "content": payLoad["content"]
# #     }
# #     # return {"data": "new post"}
   
# #     # return payLoad


# # # Payload - Whatever data the client sends in the request body (JSON in this case) will be stored inside payload.
# # # Dict - It tells FastAPI (and other developers) that payload should be a dictionary.
# # # Body - Body(...) tells FastAPI to expect data from the request body (instead of from the query string or URL path).
# # # If the client doesn’t send a body → FastAPI will return a 422 Unprocessable Entity error. If the client sends valid JSON → FastAPI automatically parses it into a Python dict.
# # # 2. PYDANTIC MODEL

# # # Now, lets tell the front end what a new post should look like in terms of the data we want
# # # 1. Title str. 2. Content str, category, number 

# # # PUBLISHED
# # @app.post("/createposts")   
# # def create_posts(new_post: Post):
# #     print(new_post.published)              # shows Pydantic model
# #     return {"data": new_post}

# # RATING
# @app.post("/posts")
# def create_posts(new_post: Post):
#     print(new_post.rating)   
#     print(new_post.dict())           # shows 
#     return {"data": new_post}

# # PYDANTIC MODEL TO DICTIONARY
# # print(new_post.dict())






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

# @app.post("/posts")
# # status_code=status.HTTP_201_CREATED )
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
# def get_post(id:int, response: Response):
#     post = find_post(id)
#     if not post:
#         response.status_code = status.HTTP_404_NOT_FOUND    
#     return {"message": f"Post with id {id} was not found"}

#     return {"post_detail": post}
# # # Validation to ensure whatever data is passed called be converted tp an integer. The way its done above. 

# # # EXAMPLE
# # # If you want to get the post with ID 1, you would send a GET request to /posts/1
# # # If you want to create a new post, you would send a POST request to /posts with the post data in the body
# # # If you want to update the post with ID 1, you would send a PUT request to /posts/1 with the updated post data in the body

# # # 


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
