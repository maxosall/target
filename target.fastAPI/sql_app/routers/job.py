from fastapi import Depends, status, HTTPException, APIRouter
from http.client import HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schema, oauth2

router =APIRouter(
  prefix="/jobs",
  tags=["jobs"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.JobOutput)
def create_job(job: schema.JobCreate, db: Session=Depends(get_db),
          current_user:int= Depends(oauth2.get_current_user)):
  
  new_job= models.Job(user_id= current_user.id,**job.dict())
  db.add(new_job)
  db.commit()
  db.refresh(new_job)
  return new_job