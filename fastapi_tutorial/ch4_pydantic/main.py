from fastapi import FastAPI,status
from typing import Optional
from pydantic import BaseModel
from model import *
app= FastAPI()


#defining the request body
@app.post("/book")
async def create_book(book:Book):
    return book

# class BookResponse(BaseModel):
#     title:str
#     author:str
#     id:int

# @app.get("/allbooks")
# async def read_all_books()->list[Book]:
#     return [{
#         "id":1,
#         "title": "1984",
#     "author": "George Orwell",
#     "year":2002},
#     {
#         "id": 2,
#     "title": "The Great Gatsby",
#     "author": "F. Scott Fitzgerald",
#     "year":2002,
#     },
#     ]

#*********  or *********
class BookResponse(BaseModel):
    # id:int
    title:str=Field(min_length=1,max_length=50)
    author:str
    year:int=Field(gt=1900,lt=2100)

@app.get("/allbooks", response_model= list[BookResponse])
async def read_all_books() -> dict:
    return [{"author":"hindi",
            "year":2002,
            "id":2,
            "title":"kuxx bhi"}]

