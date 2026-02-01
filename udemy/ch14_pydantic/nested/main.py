from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel,Field

app = FastAPI()

## Nested BOdy Model
# SubModel
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

# #Model use Submodel
# class Product(BaseModel):
#     name:str = Field(
#         title="product name ",
#         description="The name of the product",
#         max_length=100,
#         min_length=3,
#         pattern="^[A-Za-z)-9 ]+$"
#     )
#     price:float=Field(
#         title="product Price",
#         gt=5,
#         description="The price of the product in USD,must be greater than the zero"
#     )    
#     stock:int | None =Field(
#         default=None,
#         gt=0,
#         description="The number of item in stock, must be non-negative"
#     )
#     category:Category | None = Field(default=None,
#                                     title="product Category",
#                                      description="The category to which the product belongs" )

# @app.post("/product")
# async def create_product(product:Product):
#     print(f'"product":{product}')
#     return {"product":product}

### Attribute with lists of submodels
class Product(BaseModel):
    name:str = Field(
        title="product name ",
        description="The name of the product",
        max_length=100,
        min_length=3,
        pattern="^[A-Za-z)-9 ]+$"
    )
    price:float=Field(
        title="product Price",
        gt=5,
        description="The price of the product in USD,must be greater than the zero"
    )    
    stock:int | None =Field(
        default=None,
        gt=0,
        description="The number of item in stock, must be non-negative"
    )
    category:list[Category] | None=Field(
                                    default=None,
                                    title="product Category",
                                    description="The category to which the product belongs"
                                    )

@app.post("/product")
async def create_product(product:Product):
    print(f'"product":{product}')
    return {"product":product}