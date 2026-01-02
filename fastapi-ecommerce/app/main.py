from fastapi import FastAPI,HTTPException,Query
from service.products import *
app = FastAPI()

@app.get("/")
def root():
    return "Hii Abhay"

# @app.get("/products/{id}")
# def get_products(id:int):
#     print("fds")
#     products=["brush","Laptop","Mouse","Kya hal chal"]
#     return (products[id] 
#     if products[id]
#     else HTTPException(status_code=404,detail="no product Found"))

# @app.get("/products")
# def get_products():
#     print(get_all_products.products.id)
#     return get_all_products()

# @app.get("/products")
# def list_products(
#     title:str=Query(
#     default=None,
#     min_length=1,
#     max_length=50,
#     description="Search By Product title(case insenstive)",
#     )
# ):
#     products = get_all_products()
#     if title:
#         needle = title.strip().lower()
#         products = [p for p in products if needle in p.get("title","").lower()]
#         if not products:
#             raise HTTPException(status_code=404,detail=f"No Product found matching title = {title}"
# )
#     total = len(products)
#     return {
#         "total":total,
#         "items":products
#     }

@app.get("/products")
def list_products(
    title: str = Query(
        default=None,
        min_length=1,
        max_length=50,
        description="Search By Product title (case insensitive)",
    )
):
    data = get_all_products()          # already a dict
    products = data["products"]        # extract list

    if title:
        needle = title.strip().lower()
        products = [
            p for p in products
            if needle in p.get("title", "").lower()
        ]

        if not products:
            raise HTTPException(
                status_code=404,
                detail=f"No product found matching title = {title}"
            )

    return {
        "total": len(products),
        "items": products
    }
