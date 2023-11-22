from fastapi import Depends, status, HTTPException, APIRouter
from http.client import HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schema, oauth2

router =APIRouter(
  prefix="/jobs",
  tags=["jobs"]
)

@router.post("/")
#def create_post(payload: dict = Body(...)):
async def create_post(
          current_user_id:int= Depends(oauth2.get_current_user)):
  

  print(current_user_id)
  return {"title": "maxo sall"}