from pydantic import BaseModel, Field,field_validator

from typing import Optional

class UserCreate(BaseModel):
    name : str
    age :  int
    email : str
    password : str
    role : str = "user"

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("NAme can't be empty")
        return value

class CustomerCreate(BaseModel):
    name : str
    email : str
    
class UserResponse(BaseModel):
    id : int

class Address(BaseModel):
    city : str
    state : str
    pincode : str

class ProductCreate(BaseModel):
    name : str = Field(min_length=4)
    price : int = Field(gt=10)
    category : Optional[str]
    available : bool = True
    warehouse : Address
    