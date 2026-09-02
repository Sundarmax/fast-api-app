from fastapi import FastAPI, HTTPException
from model import UserCreate, UserResponse, ProductCreate

app = FastAPI()

@app.get("/")
def home(): #handler
    return { "name": "hello"}

@app.get("/users/{user_id}", response_model=UserResponse) #path parameters & limit fields in response.
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return {
        "id" : user_id,
        "name": "sundar",
        "pwd":  "12345"
    }
    
@app.get("/users") #query paramerts
def get_users(limit: int=10, active: bool=True):
    return {
        "limit" : limit,
        "active": active
    }
@app.post("/users") #post request with pydantic validation.
def create_user(user : UserCreate):
    return user

@app.get("/products")
def get_products():
    return {
        "Should return all the products"
    }

@app.get("/products/{product_id}")
def get_product(product_id :  int):
    return {
        "id" : product_id,
        "name" : "toothpaste",
        "price" : 25
     }
    
@app.post("/products")
def create_product(product : ProductCreate ):
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id : int):
    return {
        "id" : product_id,
        "message":  "deletion is done"
    }