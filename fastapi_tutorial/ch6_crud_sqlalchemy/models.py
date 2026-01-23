from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel,EmailStr,field_validator
from typing import Optional
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

class UserBody(BaseModel):
    name:str
    email:EmailStr

    @field_validator("name")
    def namevalidation(cls,value:str):
        if not (value.startswith("a") and value.endswith("y")):
            raise ValueError(" name not start is a or not end with Z")
        return value
    
