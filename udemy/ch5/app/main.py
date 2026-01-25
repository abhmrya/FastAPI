from fastapi import FastAPI
from enum import Enum
app = FastAPI()

## predefine values

# #Define an Enum class with allowed product categories
# class ProductCategory(str,Enum):
#     book = "books"
#     clothing="clothing"
#     electronics="electronics"

# #use the Enum as the path parameter
# @app.get("/product/{category}")
# async def get_product(category:ProductCategory):
#     return {"response":"product fetchhed","category":category}

## Working with python enumerations


class ProductCategory(str,Enum):
    book = "books"
    clothing="clothing"
    electronic="electronic"

@app.get("/product/{category}")
async def get_product(category:ProductCategory):
    if category== ProductCategory.book:
        return {"category":category,"message":"Book are awesome!"}
    elif category=="clothing":
        return {"category":category,"message":"good clothing"}
    elif category==ProductCategory.electronic.value:
        return {"category":category,"message":"good electronic product"}
        
    else:
        return {"category":category,"message":"Unknown category"}