from fastapi import FastAPI,Query,Path
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

## basic path parameter
# @app.get("/products/{product_id}")
# async def get_product(product_id:int):
#     for product  in PRODUCTS:
#         if product['id']==product_id:
#             return product
#         return {"error":"product not found"}
    
## Numeric Validation 
# @app.get("/products/{product_id}")
# async def get_product(product_id:Annotated[int,Path(ge=1)]):
#     for product  in PRODUCTS:
#         if product['id']==product_id:
#             return product
#     return {"error":"product not found"}

## Adding Metadata with path
# @app.get("/products/{product_id}")
# async def get_product(product_id:Annotated[int,Path(title="The ID of the product",description="this is product id")]):
#     for product  in PRODUCTS:
#         if product['id']==product_id:
#             return product
#     return {"error":"product not found"}

## COmbining Pathh and Query parameters
@app.get("/products/{product_id}")
async def get_product(product_id:Annotated[int,Path(gt=0,le=100)],
                      search:Annotated[str | None,Query(max_length=20)]=None):
    for product  in PRODUCTS:
        if product['id']==product_id:
            if search and search.lower() not in product["title"].lower():
                return {"error":"Product does not match serch term"}
            return product
    return {"error":"product not found"}
