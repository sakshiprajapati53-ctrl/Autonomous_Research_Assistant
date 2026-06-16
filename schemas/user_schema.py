from pydantic import BaseModel,EmailStr,ConfigDict
# Pydantic Schema = API ke data ka blueprint (structure + validation rules)

# user response schema
class UserCreate(BaseModel):
    name : str
    email : EmailStr
    password : str

class Userlogin(BaseModel):
    email : EmailStr
    password : str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str