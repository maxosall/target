from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schema
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


@app.get("/users/", response_model=list[schema.UserBase])
def read_users(db: Session = Depends(get_db)):
  users = crud.get_users(db)
  return users


@app.get("/users/{user_id}", response_model=schema.UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
  db_user = crud.get_user(db, user_id=user_id)
  if db_user is None:
    raise HTTPException(status_code=404, detail="User not found")
  return db_user

@app.post("/users/", response_model=schema.UserBase)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
  new_user = crud.get_user_by_email(db, email=user.email)
  if new_user:
    raise HTTPException(status_code=400, detail="Email already registered")
  return crud.create_user(db=db, user=user)


@app.post("post/")
#def create_post(payload: dict = Body(...)):
async def create_post(new_post: schema.Post):
  new_post.title = 'new tutorial'

  print(new_post)
  return {"title": "maxo sall"}