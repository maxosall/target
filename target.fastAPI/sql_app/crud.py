from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from datetime import date
from . import models, schema


def get_users(db: Session):
  return db.query(models.User).all()

def get_user_by_email(db: Session, email: str):
  return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session, user_id: int):
  return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schema.UserCreate):
  fake_hashed_password = user.password + "notreallyhashed"
  user.password=fake_hashed_password
  new_user = models.User(**user.dict())
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user