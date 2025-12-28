from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

# @app.get('/blog')
# def index(limit=10,published:bool=True,sort:Optional[str]=None):
#     # return published
#     if published:
#         return {'data':f'{limit} published blog from the db'}
#     else:
#         return {'data':f'{limit} blog from the db'}

# @app.get('/about')
# def about():
#     return {'data':{'about page'}}

# @app.get('/blog/{id}')
# def show(id:int ):
#     #fetch blog with id = id
#     return {'data':id}

# @app.get('/blog/unpublished')
# def unpublished():
#     return {'data':'all unpublish blogs'}

# @app.get('/blog/{id}/comment')
# def comment(id):
#     #fetch coming blog with id = id
#     return {'data':{'3','1','2'}}

class Blog(BaseModel):
    title:str
    body:str
    published_at:Optional[bool]
    

@app.post('/blog')
def create_blog(request:Blog):
    # return request
    return {'data': f'blog is created with title as {request.title}'}

# @app.post('/blog/{id}')
# def create_blog(id):
#     print({'data': f'blog id is {id}'})