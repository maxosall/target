from fastapi import Depends, status, HTTPException, APIRouter
from http.client import HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schema

router =APIRouter(
  prefix="/jobs",
  tags=["jobs"]
)

@router.post("/")
#def create_post(payload: dict = Body(...)):
async def create_post(new_post: schema.Post):
  new_post.title = 'new tutorial'

  print(new_post)
  return {"title": "maxo sall"}