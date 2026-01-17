from fastapi import FastAPI,status
from pydantic import BaseModel
from typing import List
from fastapi.exceptions import HTTPException


app = FastAPI()

books=[
  {
    "id": 101,
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "publisher": "Pan Books",
    "publish_date": "1979-10-12",
    "page_count": 224,
    "language": "English"
  },
  {
    "id": 102,
    "title": "1984",
    "author": "George Orwell",
    "publisher": "Secker & Warburg",
    "publish_date": "1949-06-08",
    "page_count": 328,
    "language": "English"
  },
  {
    "id": 103,
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "publisher": "T. Egerton, Whitehall",
    "publish_date": "1813-01-28",
    "page_count": 432,
    "language": "English"
  },
  {
    "id": 104,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "publisher": "J. B. Lippincott & Co.",
    "publish_date": "1960-07-11",
    "page_count": 336,
    "language": "English"
  },
  {
    "id": 105,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "publisher": "Charles Scribner's Sons",
    "publish_date": "1925-04-10",
    "page_count": 180,
    "language": "English"
  }
]
class Book(BaseModel):
    id:int
    title:str
    author:str
    publisher:str
    publish_date:str
    page_count:int
    language:str

class BookUpdateModel(BaseModel):
    title:str
    author:str
    publisher:str
    page_count:int
    language:str

@app.get('/books',response_model=List[Book])
async def get_all_bpooks():
    return books

@app.post('/books',status_code=status.HTTP_201_CREATED)
async def create_a_bpooks(book_data:Book)->dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get('/book/{book_id}')
async def get_book(book_id:int)->dict:
    for book in books:
        if book["id"]==book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found")
    

@app.patch('/book/{book_id}')
async def update_book(book_id:int,book_update_data:BookUpdateModel)->dict:
    for book in books:
        if book['id']==book_id:
            book['title']=book_update_data.title
            book['publisher']=book_update_data.publisher
            book['page_count']=book_update_data.page_count
            book['language']=book_update_data.language

            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")

@app.delete('/book/{book_id}')
async def delete_book(book_id:int)->dict:
    for key,book in enumerate(books):
        if book['id']==book_id:
            books.pop(key)
            return {"message":"successfuly delete book"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)