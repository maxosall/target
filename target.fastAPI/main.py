from fastapi import FastAPI
from sql_app import models
from sql_app.database import engine
from sql_app.routers import user, job, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def test():
  return {'data':'this test 123'}

app.include_router(user.router)
app.include_router(job.router)
app.include_router(auth.router)
