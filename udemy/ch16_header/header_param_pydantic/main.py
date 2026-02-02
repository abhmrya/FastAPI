from fastapi import FastAPI,Header,Depends
from typing import Annotated
from pydantic import BaseModel,Field

app= FastAPI()
## Header with a Pydantic Model

# class productHeaders(BaseModel):
#     authorization:str
#     accept_language:str | None =None
#     x_tracking_id:list[str] = []

# # @app.get("/products")
# # async def get_product(headers:Annotated[productHeaders,Header()]):
# #     return {
# #         "headers":headers
# #     }

# @app.get("/products")
# async def get_product(headers:Annotated[productHeaders,Header(),Depends()]):
#     return {
#         "headers":headers
#     }
# curl -H "Authorization: Bearer token123" -H "Accept-Language:en-US" -H "X-Tracking-Id: track1" -H "X-Tracking-Id: track2" http://127.0.0.1:8000/products

class productHeaders(BaseModel):
    model_config={"extra":"forbid"}
    authorization:str
    accept_language:str | None =None
    x_tracking_id:list[str] = []

@app.get("/products")
async def get_product(headers:Annotated[productHeaders,Header(),Depends()]):
    return {
        "headers":headers
    }