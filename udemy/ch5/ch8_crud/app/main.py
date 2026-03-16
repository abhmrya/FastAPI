from fastapi import FastAPI,HTTPException,status

app =FastAPI()

PRODUCTS=[
  {
    "id": 1,
    "title": "Laptop",
    "price": 999.99,
    "description": "A high-performance laptop with 16GB RAM and a 1TB SSD."
  },
  {
    "id": 2,
    "title": "Smartphone",
    "price": 549.00,
    "description": "A popular smartphone model known for its camera quality and fast processor."
  },
  {
    "id": 3,
    "title": "Headphones",
    "price": 199.50,
    "description": "Noise-cancelling over-ear headphones with 30 hours of battery life."
  },
  {
    "id": 4,
    "title": "Keyboard",
    "price": 75.25,
    "description": "A mechanical keyboard with customizable RGB backlighting."
  },
  {
    "id": 5,
    "title": "Monitor",
    "price": 245.80,
    "description": "A 27-inch 4K monitor perfect for professional use and gaming."
  }
]

#GET Request
## read or fetch Al Data
@app.get("/product")
async def allProduct():
    return PRODUCTS

@app.get("/product/{id}")
async def single_product(id:int):
    for product in PRODUCTS:
        if product["id"]==id:
            print(product)
            return product
    raise HTTPException(detail="product not found",status_code=status.HTTP_404_NOT_FOUND)
    # if(id==PRODUCTS.get(id)):
    #     return PRODUCTS.id.value

#POST REquest
## create or Insert Data
@app.post("/product")
async def create_product(product:dict):
    PRODUCTS.append(product)
    return {"status":"created","new_product":product}

#PUT REquest
## UPDate COmplete Data

@app.put("/product/{product_id}")
async def update_product(product_id:int, new_updated_product:dict):
    for product in PRODUCTS:
        if(product["id"]==product_id):
            product.update(new_updated_product)
            return {"response":"product updated","product":product}
    raise HTTPException(detail="product not found",status_code=status.HTTP_404_NOT_FOUND)

# DELETE Request
## DELETE product 

@app.delete("/product/{product_id}")
async def delete_product(product_id:int):
    for index,product in enumerate(PRODUCTS):
        if product["id"]==product_id:
            PRODUCTS.pop(index)
            return {"status":"deleted"}