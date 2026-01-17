from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
app = FastAPI()

my_post=[{"title":"title of post 1","content":"content of post 1","id":1},
         {"title":"pizza1","content":"i like pizza","id":2}]

def find_post(id):
    for p in my_post:
        if p["id"]==id:
            return p
class post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None

@app.get("/")
async def root():
    return {"message" : "hello world"}

@app.get("/posts")
def get_posts():
    return {"data":my_post}

@app.post("/posts")
def create_posts(post:post):
    post_dict = post.dict()
    post_dict['id']=randrange(0,1000000)
    my_post.append(post_dict)
    return {"data":post_dict}

# @app.post("/createposts")
# def create_posts(payload:dict = Body(...)):
#     print(payload)
#     return {"new_post" : f"title{payload['title']} content:{payload['content']}"}



# @app.post("/createposts")
# def create_posts(new_post:post):
#     post_dict = post.dict()
#     post_dict['id']=random.rando
#     my_post.append(post.dict())
#     return {"data":new_post}


#title str,content str,category,,Bool

@app.get("/posts/{id}")
def get_post(id):
    print(type(id))
    post = find_post(int(id))
    return {"post_details":post}