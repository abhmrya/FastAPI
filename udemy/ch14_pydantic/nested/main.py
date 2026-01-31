from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel,Field

app = FastAPI()

## Nested BOdy Model
class Category(BaseModel):
    name:str = Field(
        title="category name ",
        description="The name of the product category",
        max_length=50,
        min_length=1
    )
    description:str | None = Field(
        default=None,
        title="category Description of the category",
        max_length=50

    )