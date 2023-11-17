from pydantic import BaseModel


class Post(BaseModel):
  title: str
  content: str



class UserBase(BaseModel):
  email: str


class UserCreate(UserBase):
  password: str


class Profile(BaseModel):
  first_name : str 
  last_name : str 
  user_id : int
  address : str 
  resume : str     
  
