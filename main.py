from fastapi import FastAPI
from model import UserCreate, UserResponse

app = FastAPI()

@app.get("/")
def home(): #handler
    return {"hello"}

@app.get("/users/{user_id}", response_model=UserResponse) #path parameters & limit fields in response.
def get_user(user_id: int):
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
