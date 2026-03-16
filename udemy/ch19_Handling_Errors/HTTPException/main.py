from fastapi import FastAPI,HTTPException

app = FastAPI()

items = {
    "apple":"A juice fruit",
    "Banana":"A yellow delight"
    }

#using HTTpEzxeption
# @app.get("/items/{item_id}")
# async def read_item(item_id : str):
#     if item_id not in items:
#         raise HTTPException(status_code=404,detail="Item not found")
#     return items[item_id]

#Adding coustom header
@app.get("/items/{item_id}")
async def read_item(item_id : str):
    if item_id not in items:
        raise HTTPException(status_code=404,
                            detail="Item not found",
                            headers={"X-error-type":"itemmissing"})
    return items[item_id]