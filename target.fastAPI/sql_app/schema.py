from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class Token(BaseModel):
  access_token: str
  token_type:str

class TokenData(BaseModel):
  id: Optional[int]  = None

class Post(BaseModel):
  title: str
  content: str

class JobBase(BaseModel):
  title: str
  decription: str
  max_salary: Optional[float] = None
  min_salary: Optional[float] = None


class JobCreate(JobBase):
  pass

class JobOutput(JobBase):
  user_id: int
  created_at: Optional[datetime]=None
  updated_at: Optional[datetime]= None

class UserBase(BaseModel):
  email: EmailStr


class UserCreate(UserBase):
  password: str

class UserLogin(UserCreate):
  pass
class UserOutput(UserBase):
  created_at: Optional[datetime] = None
  updated_at: Optional[datetime] = None
  id :int

  class Config:
    from_attributes = True

class Profile(BaseModel):
  first_name : str 
  last_name : str 
  user_id : int
  address : str 
  resume : str     
  
