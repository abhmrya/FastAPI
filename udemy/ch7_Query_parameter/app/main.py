from fastapi import FastAPI

app= FastAPI()

# #single Query parameter
# @app.get("/product")
# async def product(category:str):
#     return {"status":"ok","category":category}

# #multiple Query parameter
# @app.get("/product")
# async def product(category:str,limit:int):
#     return {"status":"ok","category":category,"limit":limit}

# #DEfault Query parameter
# @app.get("/product")
# async def product(category:str,limit:int=10):
#     return {"status":"ok","category":category,"limit":limit}

# #Optional Query parameter
# @app.get("/product")
# async def product(limit:int,category:str | None=None):
#     return {"status":"ok","category":category,"limit":limit}

#path and  Query parameter
@app.get("/product/{year}")
async def product(year:str,category:str):
    return {"status":"ok","category":category,"year":year}

