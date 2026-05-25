from sqlalchemy import BaseModel


class RegisterRequest(BaseModel):
    full_name: str
    email: str
    mobile_number: str
    password: str


class LoginRequest(BaseModel):
    mobile_number: str
    password: str

class UserResponse(BaseModel):
    id: int
    fullname: str
    email: str
    mobile_number: str
    status: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"
    user: UserResponse
