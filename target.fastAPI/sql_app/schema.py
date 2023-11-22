from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class Token(BaseModel):
  access_token: str
  token_type:str

class TokenDta(BaseModel):
  id: Optional[str]  = None

class Post(BaseModel):
  title: str
  content: str

class UserBase(BaseModel):
  email: EmailStr


class UserCreate(UserBase):
  password: str

class UserLogin(UserCreate):
  pass
class UserOutput(UserBase):
  created_at: Optional[datetime] = None
  updated_at: Optional[datetime] = None

  class Config:
    from_attributes = True

class Profile(BaseModel):
  first_name : str 
  last_name : str 
  user_id : int
  address : str 
  resume : str     
  
