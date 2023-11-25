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






#? --------- *> PROFILE'S SCHEMA <* --------
class ProfileBase(BaseModel):
  first_name: str
  last_name: str
  phone_number: str
  address: Optional[str]
  resume: Optional[str]
   

class ProfileCreate(ProfileBase):
  pass


class ProfileOutput(ProfileCreate):
  created_at : Optional[datetime] = None
  updated_at : Optional[datetime] = None
  



#? --------- *> JOB'S SCHEMA <* --------
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




#? --------- *> USER'S SCHEMA <* --------
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

