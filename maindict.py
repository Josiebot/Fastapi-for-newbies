# # USING A DICT MODEL
# from fastapi import FastAPI, Body

# app = FastAPI()

# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     # Access via dictionary keys
#     title = payload["title"]
#     content = payload["content"]
    
#     print(title, content)
    
#     return {"title": title, "content": content}


# # Pros:

# # Simple, just a dictionary.

# # No extra class needed.

# # Cons:

# # No validation: If the JSON is missing "title" or "content", FastAPI will try to access a key that doesn’t exist → KeyError.

# # No type checking: "title": 123 would be accepted even though it should be a string.

# # You must manually parse, validate, and document the fields.

# # Harder to maintain for larger APIs with many fields.
# # Client can send any data they want
# # The data does not get validated, we do not get all the values from the body easily. 