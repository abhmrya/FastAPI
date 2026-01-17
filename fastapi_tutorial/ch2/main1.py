from fastapi import FastAPI,Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message":"hello world"}

# @app.get('/greet/{name}')
# async def greet_name(name:str,age:int)->dict:
#     return {"message":f"hello {name}","age":age}

@app.get('/greet')
async def greet_name(name:Optional[str]="User",
                     age:int=0)->dict:
    print(name,age)
    return {"message":f"hello {name}","age":age}

class bookCreateModel(BaseModel):
    title : str
    author : str


@app.post('/create_book')
async def create_book(book_data:bookCreateModel):
    return {
        "title":book_data.title,
        "author":book_data.author
    }

@app.get('/get_headers',status_code=201)
async def get_headers(
    accept:str=Header(None),
    content_type:str=Header(None),
    cookie:str=Header(None),
    user_agent:str=Header(None),
    host:str=Header(None)):
    print(cookie)
    print(accept)
    print(content_type)
    print(host)
    print(user_agent)
    request_headers={}
    request_headers["Accept"]=accept
    request_headers["content-type"]=content_type
    request_headers["cookie"]=cookie
    request_headers["user-Agent"]=user_agent
    request_headers["host"]=host
    return request_headers