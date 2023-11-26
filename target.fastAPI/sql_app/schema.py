from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr

class Token(BaseModel):
  access_token: str
  token_type:str

class TokenData(BaseModel):
  id: Optional[int]  = None

class Post(BaseModel):
  title: str
  content: str




#? --------- *> JOB'S SCHEMA <* --------
class JobBase(BaseModel):  
  title: str
  decription: str
  max_salary: Optional[float] = None
  min_salary: Optional[float] = None

  class Config:
    from_attributes = True

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





#? --------- *> PROFILE'S SCHEMA <* --------
class ProfileBase(BaseModel):
  first_name: str
  last_name: str
  phone_number: str
  address: Optional[str] = None
  resume: Optional[str] = None
   

class ProfileCreate(ProfileBase):
  # class Config:
  #   from_attributes = True
  pass


class ProfileOutput(ProfileCreate):
  created_at : datetime
  updated_at : Optional[datetime] = None
  

class ProfileDetails(ProfileOutput):
  # jobs: List["JobOutput"]
  user: UserOutput

  class Config:
    from_attributes = True