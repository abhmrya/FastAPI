from pydantic import BaseModel,Field

# creating a model
class Book(BaseModel):
    id:int
    title:str=Field(min_length=1,max_length=50)
    author:str
    year:int=Field(gt=1900,lt=2100)

