from fastapi import FastAPI
from . import models, schema
from .database import engine
from . routers import users, jobs

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def test():
  return {'data':'this test 123'}

app.include_router(users.router)
app.include_router(jobs.router)

