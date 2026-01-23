from pydantic import BaseModel,EmailStr
from typing import Optional
from sqlalchemy.orm import Mapped,mapped_column

class Tweet(BaseModel):
    content:str
    hashtags:list[str]

class User(BaseModel):
    name:str
    email:EmailStr
    # age:Optional[int]
    # tweets:list[Tweet] | None=None