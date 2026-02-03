from fastapi import FastAPI 
from pydantic import BaseModel
from typing import List,Any,Optional

app = FastAPI()

## Excludeing Unset Default Values

products_db ={
    "1":{"id":"1","name":"Laptop","price":999.99,"stock":10,"is_Active":True},
    "2":{"id":"2","name":"Smartphone","price":499.99,"stock":50,"is_Active":False},
}

class Product(BaseModel):
    id:str
    name:str
    price:float
    description:Optional[str] = None
    tax:float=15.0  # Default tax rate

# @app.get("/products/{product_id}",response_model=Product,response_model_exclude_unset=True)
# async def get_product(product_id:str):
#     return products_db.get(product_id,{})

# @app.get("/products/{product_id}",response_model=Product,
# response_model_include={"name","price"})
# async def get_product(product_id:str):
#     return products_db.get(product_id,{})

@app.get("/products/{product_id}",response_model=Product,response_model_exclude={"name","price"})
async def get_product(product_id:str):
    return products_db.get(product_id,{})