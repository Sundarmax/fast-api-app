from fastapi import FastAPI, HTTPException, Depends, APIRouter
from schemas.user import UserCreate, UserResponse, ProductCreate, CustomerCreate
from services import productService
from databases.session import get_db
from databases.user import User

app = FastAPI()

router = APIRouter(prefix="/v1", tags=["version1"])

# def get_db():
#     return "Database Connection"

def payment_service():
    return "External call to payment gateway"

def oauth2_Schem():
    return "Extract the bearer token from the http header"

def get_current_user(token : str = Depends(oauth2_Schem)):
    user = token # validate the token and extract it from the JWT payload & do RBAC
    return user

def get_current_user(token : str = Depends(oauth2_Schem)):
    curr_user = token # validate the token and extract it from the JWT payload & do RBAC
    if curr_user['role'] != 'admin':
        raise HTTPException(
                status_code=403,
                detail="Admin access required"
        )
    return curr_user

def get_pagination(
    page: int=1,
    limit: int=10
):
    return {
        "page": page,
        "limit": limit
    }

@app.get("/")
def home(): #handler
    return { "name": "hello"}

@app.get("/page")
def get_data(
    pagination = Depends(get_pagination)
):
    return pagination

@app.get("/payment")
async def payment():
    reponse = await payment_service()
    return reponse
# async/await doesn't make the operation itself faster; it prevents the application from sitting idle during I/O waits, allowing the event loop to make progress on other tasks.

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
def get_users(db : session =  Depends(get_db)):
    return db.query(User).all()

# @app.post("/users") #post request with pydantic validation.
# def create_user(user : UserCreate):
#     return user
@app.post("/users")
def create_user(
    user_data : CustomerCreate,
    db: session = Depends(get_db)
):
    user = User(
        name = user_data.name,
        email = user_data.email
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
@app.get("/products")
def get_products(db = Depends(get_db)): #DI - Separation of concerns and reusability.
    return {
        "db" : db
    }

@app.get("/products/{product_id}")
def get_product(product_id :  int):
    product = productService.ProductService()
    product = product.get_product_by_id(product_id)
    return product

@app.post("/products")
def create_product(product : ProductCreate ):
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id : int):
    return {
        "id" : product_id,
        "message":  "deletion is done"
    }
    
@app.post("/post")
def login():
    return {
        "access_token" : "abcd",
        "token_type" : "bearer"
    }
