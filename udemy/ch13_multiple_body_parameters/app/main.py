from fastapi import FastAPI,Body,Path
from typing import Annotated
from pydantic import BaseModel
app = FastAPI()

## Multiple BOdy Paramters
class Product(BaseModel):
    name:str
    price:float
    stock:int | None =None

class Seller(BaseModel):
    username: str
    full_name:str|None=None

# @app.post("/product")
# async def create_product(product:Product,seller:Seller):
#     print(f'"product":{product},"seller":{seller}')
#     return {"product":product,"seller":seller}


#MAke Body Optional 
# @app.post("/product")
# async def create_product(product:Product,seller:Seller | None=None):
#     print(f'"product":{product},"seller":{seller}')
#     return {"product":product,"seller":seller}

## singular values in body
# @app.post("/product")
# async def create_product(
#                         product:Product,
#                         seller:Seller,
#                         sec_key:Annotated[str,Body()]):
#     print(f'"product":{product},"seller":{seller}')
#     print(f'"secret_key":{sec_key}')
#     return {"product":product,"seller":seller,"sec_key":sec_key}


# ## Embed a singular body paramter
# ## without Embed
# @app.post("/product")
# async def create_product(product:Product):
#     return product
# {
#   "name": "string",
#   "price": 0,
#   "stock": 0
# }

## with Embed
@app.post("/product")
async def create_product(product:Annotated[Product,Body(embed=True)]):
    return product
