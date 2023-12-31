from sqlalchemy.orm import Session
from . import models, schema, utils


def get_users(db: Session):
  return db.query(models.User).all()

def get_user_by_email(db: Session, email: str):
  return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session, user_id: int):
  return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schema.UserCreate):
  hashed_password = utils.hash(user.password)
  user.password=hashed_password
  new_user = models.User(**user.model_dump())
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

def login(db: Session, user_crdentials: schema.UserLogin):
  db.query(models.User).filter(models.User.email == user_crdentials.email).first()