from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
app = FastAPI()


@app.get("/")
async def root():
    return {"message" : "hello world"}

@app.get("/posts")
def get_posts():
    return {"data":"this is your posts"}

# @app.post("/createposts")
# def create_posts(payload:dict = Body(...)):
#     print(payload)
#     return {"new_post" : f"title{payload['title']} content:{payload['content']}"}

class post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None

@app.post("/createposts")
def create_posts(new_post:post):
    print(new_post)
    print(new_post.dict())
    return {"data":new_post}


#title str,content str,category,,Bool


# 12