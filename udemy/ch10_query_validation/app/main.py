from fastapi import FastAPI,Query
from typing import Annotated
from pydantic import AfterValidator
app = FastAPI()

PRODUCTS=[
  {"id": 1,"title": "Laptop","price": 999.99,
      "description": "A high-performance " },
  { "id": 2,"title": "Smartphone laptop", "price": 549.00,
      "description": "A popular smartphone "},
  {"id": 3, "title": "Headphones q","price": 199.50,
      "description": "Noise-cancelling over-ear"}
]

#Basic Query parameter
# @app.get("/products")
# async def get_product(serach:str | None=None):
#     if serach:
#         serach_lower=serach.lower()
#         filtered_product=[]
#         for product in PRODUCTS:
#             if serach_lower in product["title"].lower():
#                 filtered_product.append(product)
#         return filtered_product
#     return PRODUCTS


# # validation without Anotated
# @app.get("/products")
# async def get_product(serach:str | None=Query(default=None,max_length=5)):
#     if serach:
#         serach_lower=serach.lower()
#         filtered_product=[]
#         for product in PRODUCTS:
#             if serach_lower in product["title"].lower():
#                 filtered_product.append(product)
#         return filtered_product
#     return PRODUCTS

# # validation with Annotated
# @app.get("/products")
# async def get_product(serach:Annotated[str | None,Query(max_length=5,min_length=3)]=None):
#     if serach:
#         serach_lower=serach.lower()
#         filtered_product=[]
#         for product in PRODUCTS:
#             if serach_lower in product["title"].lower():
#                 filtered_product.append(product)
#         return filtered_product
#     return PRODUCTS

# # validation with Annotated
# @app.get("/products")
# async def get_product(serach:Annotated[str | None,Query(min_length=3,pattern="^[a-z]+$")]=None):
#     if serach:
#         serach_lower=serach.lower()
#         filtered_product=[]
#         for product in PRODUCTS:
#             if serach_lower in product["title"].lower():
#                 filtered_product.append(product)
#         return filtered_product
#     return PRODUCTS

# ## Multiple Search Terms (List)
# @app.get("/products")
# async def get_products(serch:Annotated[list[str] | None,Query()]):
#     if serch:
#         filtered_products=[]
#         for product in PRODUCTS:
#             for s in serch:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS
    
# ## Alias parameters
@app.get("/products")
async def get_products(serch:Annotated[str | None,Query(alias="Q")]):
    if serch:
        filtered_products=[]
        for product in PRODUCTS:
            for s in serch:
                if s.lower() in product["title"].lower():
                    filtered_products.append(product)
        return filtered_products
    return PRODUCTS

## Adding  MEtadata'## Alias parameters
# @app.get("/products")
# async def get_products(serch:Annotated[str | None,Query(alias="Q",title="search Products",description="search by product title")]):
#     if serch:
#         filtered_products=[]
#         for product in PRODUCTS:
#             for s in serch:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

## Custom  validation
# def  check_valid_id(id:str):
#     if not id.startswith("lap"):
#         raise ValueError("ID must start with 'lap")
#     return id

# @app.get("/products")
# async def get_products(id:Annotated[str | None,AfterValidator(check_valid_id)]=None):
#     if id:
#         return {"id":id,"message":"VAlid product ID "}
#     return {"message":"no ID provided"}