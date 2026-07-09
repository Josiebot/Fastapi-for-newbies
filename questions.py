# PART 1- PYDANTIC/DICT
# Q1.

# Pydantic model:
# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None
# If a user sends this request:
# {
#   "title": "FastAPI Rocks!",
#   "content": "I love learning this framework."
# }

# What will print(new_post.dict()) show?

# A) {'title': 'FastAPI Rocks!', 'content': 'I love learning this framework.'}
# B) {'title': 'FastAPI Rocks!', 'content': 'I love learning this framework.', 'published': True, 'rating': None}
# C) {'title': 'FastAPI Rocks!', 'content': 'I love learning this framework.', 'published': False, 'rating': 0}
# D) Error, because rating is missing.

# ✅ Answer: B
# Explanation:

# published defaults to True since the user didn’t provide it.

# rating is Optional and defaults to None.

# Pydantic fills in missing values with defaults → so the dict will have all fields.

# Q2.

# What does this line mean?

# post: Post


# A) post is just a normal Python dictionary.
# B) FastAPI will validate the incoming request body against the Post schema.
# C) post is always a string.
# D) It means post must come from query parameters.

# ✅ Answer: B
# Explanation:

# When you type hint post: Post, FastAPI uses the Pydantic model to:

# validate the incoming JSON body,

# auto-convert it into a Post object,

# and give you access to its fields like post.title.

# Q3.

# What happens if a user sends this body:

# {
#   "title": "My Test",
#   "content": "Missing published",
#   "published": "yes"
# }


# A) FastAPI accepts it and sets published = True.
# B) FastAPI rejects it with a 422 Unprocessable Entity error.
# C) FastAPI silently ignores published since it’s wrong.
# D) FastAPI converts "yes" into False.

# ✅ Answer: B
# Explanation:

# published is expected to be a bool (True/False).

# "yes" is a string → invalid type.

# FastAPI + Pydantic validation will reject the request with a 422 error.

# Q4.

# Why use Pydantic models instead of plain dictionaries?

# A) They are faster than dictionaries.
# B) They automatically validate data and provide defaults.
# C) They remove the need to use JSON.
# D) They replace the need for databases.

# ✅ Answer: B
# Explanation:

# Pydantic ensures data matches the schema (title must be a string, etc.).

# Provides default values if fields are missing.

# Makes your API safer and easier to debug.

# Q5.

# If you send this body:

# {
#   "title": "First Post",
#   "content": "Testing rating field",
#   "rating": 5
# }


# What will FastAPI accept as the value of rating?

# A) None
# B) 5 (int)
# C) "5" (string)
# D) Error, because rating is Optional

# ✅ Answer: B
# Explanation:
# Even though rating is Optional, you can still provide a value. FastAPI will validate it and assign 5 as an int.

# Q6.

# What’s the difference between:

# published: bool = True
# rating: Optional[int] = None


# A) Both act the same, there is no difference.
# B) published must always be provided by the user, but rating is optional.
# C) published has a default value, while rating can either be an int or missing (None).
# D) rating is always required, published is not.

# ✅ Answer: C
# Explanation:

# published defaults to True unless overwritten.

# rating can be provided, but if missing → defaults to None.

# Q7.

# What happens if you call this endpoint with /posts/abc?

# @app.get("/posts/{id}")
# def get_post(id: int):
#     return {"id": id}


# A) FastAPI converts "abc" into 0.
# B) FastAPI rejects the request with a 422 error.
# C) FastAPI treats "abc" as None.
# D) It accepts "abc" as a string.

# ✅ Answer: B
# Explanation:

# id is typed as int.

# "abc" cannot be converted into an integer.

# FastAPI automatically validates and returns a 422 Unprocessable Entity error.

# Q8.

# Look at this code:

# @app.post("/posts")
# def create_posts(post: Post):
#     return {"data": post.dict()}


# If the client sends:

# {
#   "title": "Learning",
#   "content": "FastAPI is cool"
# }


# What does the server return?

# A) {"data": {"title": "Learning", "content": "FastAPI is cool"}}
# B) {"data": {"title": "Learning", "content": "FastAPI is cool", "published": True, "rating": None}}
# C) Error, because published and rating are missing.
# D) Only {"data": "FastAPI is cool"}

# ✅ Answer: B
# Explanation:
# FastAPI + Pydantic add default values for published and rating.

# Q9.

# Why do we sometimes use raise HTTPException(...) instead of just returning a dictionary like {"error": "not found"}?

# A) It automatically sets the correct HTTP status code (like 404).
# B) It’s faster than returning a dictionary.
# C) It prevents the server from crashing.
# D) It hides the error from the client.

# ✅ Answer: A
# Explanation:

# Returning {"error": "not found"} always sends back a 200 OK.

# raise HTTPException tells FastAPI: “Send a real error response with the correct code (e.g., 404).”

# Q10.

# What does this line do?

# status_code=status.HTTP_201_CREATED


# A) Tells FastAPI to always send 201 after creating a post.
# B) Changes the ID of the post to 201.
# C) Only works if the user sends status=201 in the body.
# D) Tells FastAPI to reject requests unless ID = 201.

# ✅ Answer: A
# Explanation:
# By default, POST returns 200 OK. But 201 Created is the correct HTTP status when a new resource is created.

# Q11.

# Which of the following BEST describes the role of my_posts in your app?

# A) It is a database.
# B) It is a temporary in-memory list storing posts until you restart the server.
# C) It permanently saves posts across restarts.
# D) It’s only used for GET requests.

# ✅ Answer: B
# Explanation:
# my_posts is just a Python list acting like a fake database. Once you stop the app, all posts are lost.

# Q12.

# In your function:

# def find_post(id: int):
#     for p in my_posts:
#         if p["id"] == id:
#             return p
#     return None


# If no post matches the id, what is returned?

# A) 0
# B) None
# C) Empty dictionary {}
# D) "Post not found"

# ✅ Answer: B
# Explanation:
# The loop returns the post if found, but if none match → the function explicitly returns None.

# PART 2
# 1. FastAPI Basics

# Q: What does app = FastAPI() do?
# A) Creates a Python class
# B) Creates a FastAPI application instance
# C) Runs a web server
# D) Defines a route

# ✅ Answer: B
# Explanation: app = FastAPI() creates an application instance that acts as the core of your API.

# 2. CRUD in FastAPI

# Q: Which HTTP method is used to create new resources in FastAPI?
# A) GET
# B) POST
# C) PUT
# D) DELETE

# ✅ Answer: B
# Explanation: POST requests are used for creating new data entries (like new posts).

# 3. Path Parameters

# Q: If you define @app.get("/posts/{id}") with id: int, what happens when you visit /posts/10?
# A) You get an error
# B) It returns {"id": 10}
# C) It always returns the first post
# D) It ignores the number

# ✅ Answer: B
# Explanation: FastAPI converts the {id} path parameter into an integer and returns it.

# 4. Pydantic Models

# Q: Why do we use Pydantic models in FastAPI?
# A) For styling HTML
# B) For data validation and structure
# C) For connecting to the database
# D) To generate random IDs

# ✅ Answer: B
# Explanation: Pydantic validates incoming request data and ensures it follows the expected structure.

# 5. Convert Model to Dict

# Q: What does post.dict() do?
# A) Turns a dictionary into a Pydantic model
# B) Turns a Pydantic model into a dictionary
# C) Deletes a model
# D) Generates random IDs

# ✅ Answer: B
# Explanation: .dict() converts a validated Pydantic object into a regular dictionary.

# 6. Adding IDs

# Q: Why is randrange(0, 100000) used in create_posts?
# A) To validate data
# B) To create a fake database ID
# C) To generate a random string
# D) To replace the title

# ✅ Answer: B
# Explanation: It simulates auto-generated IDs from a database.

# 7. Finding Posts

# Q: What happens if find_post(id) doesn’t find a match?
# A) It crashes the program
# B) It returns None
# C) It returns an empty string
# D) It always returns the first post

# ✅ Answer: B
# Explanation: If no post matches, the function returns None.

# 8. Index Lookup

# Q: What does find_index_post(id) return if the post is found?
# A) The post itself
# B) The index (position) in the list
# C) The title of the post
# D) Always None

# ✅ Answer: B
# Explanation: It returns the position number of the post inside my_posts.

# 9. DELETE Endpoint

# Q: What does status_code=status.HTTP_204_NO_CONTENT mean in a DELETE request?
# A) It returns the deleted post
# B) It deletes but shows a success message
# C) It deletes successfully and returns no content
# D) It means an error occurred

# ✅ Answer: C
# Explanation: 204 means the delete worked but no response body is returned.

# 10. Updating Posts

# Q: What does my_posts[index] = post_dict do in the update function?
# A) Deletes the post
# B) Replaces the old post at that position with new data
# C) Converts post_dict into JSON
# D) Ignores the update

# ✅ Answer: B
# Explanation: It updates the existing post in the list with the new values.

# 11. Uvicorn Command

# Q: After moving main.py into an app folder, which command runs the server?
# A) uvicorn main:app --reload
# B) uvicorn app.main:app --reload
# C) uvicorn app/main:app.py
# D) uvicorn run app

# ✅ Answer: B
# Explanation: FastAPI uses import paths (app.main:app), not file paths.

# 12. Special File

# Q: What does __init__.py do in the app/ folder?
# A) Creates a FastAPI app
# B) Tells Python this folder is a package
# C) Starts the Uvicorn server
# D) Defines routes

# ✅ Answer: B
# Explanation: __init__.py marks the folder as a Python package so it can be imported.