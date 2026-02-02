from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app=FastAPI()

class Product(BaseModel):
    id:int
    name:str
    price:float
    stock:int | None = None

class ProductOut(BaseModel):
    name:str
    price:float

# #Without Return Type
# @app.get("/products/")
# async def get_products():
#     return{"status" : "ok"}

# Return type annonation
# @app.get("/products/")
# async def get_products()->Product:
#     return {"id":1,"name":"Moto E","price":23.43,"stock":3}

# @app.get("/products/")
# async def get_products()->Product:
#     return {"id":1,"name":"Moto E","price":23.43}

# @app.get("/products/")
# async def get_products()->Product:
#     return {"id":1,"name":"Moto E","price":23.43,"stock":3,"description":"this is moto"}

# @app.get("/products/")
# async def get_products()->List[Product]:
#     return [{"id":1,"name":"Moto E","price":23.43,"stock":3},
#             {"id":2,"name":"Moto E","price":23.43,"stock":3},
#             {"id":3,"name":"Moto E","price":23.43,"stock":3},
#             {"id":4,"name":"Moto E","price":23.43,"stock":3}]

# @app.post("/products/")
# async def create_product(product:Product)->Product:
#     # return "hello world"
#     return product

# @app.post("/products/")
# async def create_product(product:Product)->ProductOut:
#     # return "hello world"
#     return product


class BaseUser(BaseModel):
    username:str
    full_name:str|None = None
class UserIn(BaseUser):
    password:str

@app.post("/users/")
async def create_product(user:UserIn)->BaseUser:
    return user
