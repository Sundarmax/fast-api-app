from model import ProductCreate,Address, UserCreate

# pydantic automatically does validation.
# datatype checking.
# try:
#     product = ProductCreate(
#         name="Laptop",
#         price=6,
#         category= "essential"
#     )
# except Exception as e:
#     print(e)
    
# example for the nested model.

prdt = ProductCreate(
    name= "MacBook",
    price= 11,
    category= "Laptop",
    warehouse= Address(
        city = "Bangalore",
        state= "Karnataka",
        pincode= "560001"
    )
)
print(prdt.model_dump( exclude=["price"])) #Pydantic object → dict/JSON = Serialization
user_data = {
    "name" : "",
    "age" : 21,
    "email": "smax@ac.in"
}

user = UserCreate.model_validate(user_data) ## JSON → Python/Pydantic object = Deserialization

print(user)
