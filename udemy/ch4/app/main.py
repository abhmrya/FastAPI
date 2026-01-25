from fastapi import FastAPI

app=FastAPI()

#********  string int router  ********

# @app.get("/product/{product_id}")
# async def single_product(product_id):
#     return {"response":"single data fetched","product_id":product_id}

# @app.get("/product/{product_id}")
# async def single_product(product_id:int):
#     return {"response":"single data fetched","product_id":product_id}

# @app.get("/product/{product_title}")
# async def single_product(product_title:str):
#     return {"response":"single data fetched","product_id":product_title}

###  order matters

# @app.get("/product/{product_title}")
# async def single_product(product_title:str):
#     return {"response":"single data fetched","product_id":product_title}

# @app.get("/product/rode_nt_usb")
# async def single_product():
#     return {"response":"single data fetched"}


@app.get("/product/rode_nt_usb")
async def single_product():
    return {"response":"single data fetched"}

@app.get("/product/{product_title}")
async def single_product(product_title:str):
    return {"response":"single data fetched","product_id":product_title}


## predefine values
