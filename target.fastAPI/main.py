from fastapi import FastAPI
from fastapi.params import Body
from sql_app.schema import Post

app = FastAPI()

@app.get("/")
async def home():
  return {"name": "maxo sall"}

@app.post()
#def create_post(payload: dict = Body(...)):
async def create_post(new_post: Post):
  new_post.title = 'new tutorial'

  print(new_post)
  return {"title": "maxo sall"}

