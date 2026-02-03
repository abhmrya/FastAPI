from fastapi import FastAPI
from pydantic import BaseModel
from typing import List,Any

app = FastAPI()

class Product(BaseModel):
    id:int
    name:str
    price:float
    stock:int | None = None

class ProductOut(BaseModel):
    name:str
    price:float

# ## without response model parameter
# @app.get("/products/")
# async def get_products():
#     return {"id":1,"name":"Moto E","price":33.33,"stock":5}

##with response model parameter
# @app.get("/products/",response_model=Product)
# async def get_products():
#     return {"id":1,"price":33.33,"stock":5}

# @app.get("/products/",response_model=List[Product])
# async def get_products():
#     return [
#             {"id":1,"name":"Moto E","price":33.33,"stock":5},
#             {"id":1,"name":"Moto E","price":33.33,"stock":5},
#             {"id":1,"name":"Moto E","price":33.33,"stock":5}
#         ]

# @app.get("/products/",response_model=List[Product])
# async def get_products():
#     return [
#             {"id":1,"name":"Moto E","price":33.33,"stock":5},
#             {"id":1,"name":"Moto E","price":33.33,"stock":5,"description":"desc"},
#             {"id":1,"name":"Moto E","price":33.33,"stock":5}
#         ]

# @app.post("/products/",response_model=Product)
# async def get_products(product:Product):
#     return product

# class BaseUser(BaseModel):
#     username:str
#     full_name:str|None = None
# class UserIn(BaseUser):
#     password:str

# @app.post("/users/",response_model=BaseUser)
# async def create_product(user:UserIn):
#     return user

# @app.post("/products/",response_model=Product)  #priority high
# async def get_products(product:Product)->Any:
#     return product

@app.post("/products/",response_model=None)  #desable
async def get_products(product:Product)->Any:
    return product