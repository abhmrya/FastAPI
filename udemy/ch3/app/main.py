from fastapi import FastAPI

app = FastAPI()

## GET Request
## read or fetch ALL DATA

@app.get("/product")
async def all_products():
    return {"reaponse":"all Products"}

@app.get("/product/{product_id}")
async def all_products(product_id):
    return {"reaponse":"single data fetch","product_id":product_id}

@app.post("/product")
async def create_product(new_product:dict):
    return {"response":"product created","product":new_product}

@app.put("/product/{product_id}")
async def update_product(new_update_product:dict,product_id:int):
    print(f"product_id {product_id} new_update_product {new_update_product}")
    return {"response":"Complete data Updated","product_id":product_id,"new Update product":new_update_product}

@app.delete("/product/{product_id}")
async def create_product(new_product:dict,product_id:int):
    return {"response":"product created","product":new_product}
