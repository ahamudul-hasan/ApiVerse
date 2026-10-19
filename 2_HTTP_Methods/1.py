
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message': 'Patient Management System API'}


# GET: Read data
@app.get("/products")
def get_products():
    return {"message": "Here are all products"}

# POST: Create data
@app.post("/products")
def create_product():
    return {"message": "Product created"}

# PUT: Replace data
@app.put("/products/{product_id}")
def replace_product(product_id: int):
    return {
        "message": "Product replaced",
        "product_id": product_id
    }

# PATCH: Update part of the data
@app.patch("/products/{product_id}")
def update_product(product_id: int):
    return {
        "message": "Product partially updated",
        "product_id": product_id
    }

# DELETE: Delete data
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    return {
        "message": "Product deleted",
        "product_id": product_id
    }
