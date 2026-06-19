from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class NotificationCreate(BaseModel):
    title: str
    message: str
    channel: str
    status: str
    
class NotificationStatusUpdate(BaseModel):
    status: str