from typing import List
from fastapi import Depends, status, HTTPException, APIRouter
from http.client import HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud, schema

router =APIRouter(
  prefix="/users",
  tags=["users"]
)


@router.get("/", response_model=list[schema.UserOutput])
def read_users(db: Session = Depends(get_db)):
  users = crud.get_users(db)
  return users


@router.get("/{user_id}", response_model=schema.UserOutput)
def read_user(user_id: int, db: Session = Depends(get_db)):
  db_user = crud.get_user(db, user_id=user_id)
  if db_user is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id:({user_id}) not found")
  return db_user


@router.post("/", status_code = status.HTTP_201_CREATED, 
          response_model=schema.UserOutput)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
  new_user = crud.get_user_by_email(db, email=user.email)
  if new_user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email already registered")
  return crud.create_user(db=db, user=user)
