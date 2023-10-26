from pydantic import BaseModel


class Post(BaseModel):
  title: str
  content: str

class User(BaseModel):
    email = str
    hashed_password = str
    is_active = bool
    
