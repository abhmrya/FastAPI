from fastapi import FastAPI

app=FastAPI()

# @app.get("/product/{product_id}")
# async def single_product(product_id):
#     return {"response":"single data fetched","product_id":product_id}

# @app.get("/product/{product_id}")
# async def single_product(product_id:int):
#     return {"response":"single data fetched","product_id":product_id}

@app.get("/product/{product_title}")
async def single_product(product_title:str):
    return {"response":"single data fetched","product_id":product_title}