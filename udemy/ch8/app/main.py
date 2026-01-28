from fastapi import FastAPI,HTTPException,status
app= FastAPI()

PRODUCT=[
    {
      "id": 101,
      "title": "Digital Creator Bundle",
      "book": {
        "title": "The Art of Content Creation",
        "author": "Jane Doe",
        "genre": "Education"
      }
    },
    {
      "id": 102,
      "title": "Minimalist Office Setup",
      "book": {
        "title": "Focus: The Power of Less",
        "author": "John Smith",
        "genre": "Productivity"
      }
    },
    {
      "id": 103,
      "title": "Tech Enthusiast Pack",
      "book": {
        "title": "The Future of AI",
        "author": "Dr. A. Scientist",
        "genre": "Technology"
      }
    },
    {
      "id": 104,
      "title": "Culinary Masterclass Kit",
      "book": {
        "title": "Cooking with Passion",
        "author": "Chef Marco",
        "genre": "Cookbook"
      }
    },
    {
      "id": 105,
      "title": "Fitness Transformation Kit",
      "book": {
        "title": "Active Life Daily",
        "author": "Sarah Trainer",
        "genre": "Health"
      }
    }
  ]

@app.get("/product")
def product():
    return {"response":"all data ","product":PRODUCT}

@app.get("/product/{id}")
def one_product(id:int):
    for product in PRODUCT:
        if product["id"]==id:
            return product
    raise HTTPException(detail="product is not availble",status_code=status.HTTP_404_NOT_FOUND)

@app.post("/product")
def create_product(product:dict):
    PRODUCT.append(product)
    return HTTPException(status_code=status.HTTP_201_CREATED)


@app.delete("/product/{id}")
def delete_product(id:int):
    for index,product in enumerate(PRODUCT):
        if product["id"]==id:
           PRODUCT.pop(index)
           return HTTPException(status_code=status.HTTP_201_CREATED)
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)