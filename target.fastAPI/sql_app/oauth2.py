from fastapi import FastAPI, Depends, status, HTTPException
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from . import schema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY = 'Hs3sdyf7y9ufeG4jhk3fgr4A456tr9mk84j2U98Hm0rk'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
  to_encode = data.copy()

  expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp":expire})

  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def verify_access_token(token: str, credentials_exception):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    id: str = payload.get("user_id")
    if id is None:
      raise credentials_exception
    token_data = schema.TokenData(id=id)
  except JWTError:
    raise credentials_exception
  return token_data  

def get_current_user(token:str = Depends(oauth2_scheme)):
  credentials_exception = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,
  detail=f"could not verificate credentials",
  headers={"WWW-Authenticate":"Bearer"})

  return verify_access_token(token, credentials_exception)