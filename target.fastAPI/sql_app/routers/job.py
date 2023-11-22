from fastapi import Depends, Response, status, HTTPException, APIRouter
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

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deflete_job(id:int, db: Session= Depends(get_db), 
                current_user: int = Depends(oauth2.get_current_user)):
  job = db.query(models.Job).filter(models.Job.Id == id).first()

  if job == None:
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                        detail=f"Job with id: ({id}) does not exist")
  
  if job.user_id == current_user.id:
    raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, 
                        detail=f"Not authorized to perform the requested action")

  job.delete(Synchronize_seasion = False)
  db.commit()
  return Response(status_code = status.HTTP_202_ACCEPTED)

@router.put("/", status_code=status.HTTP_201_CREATED, response_model=schema.JobOutput)
def update_job(updated_job: schema.JobCreate, db: Session=Depends(get_db),
          current_user:int= Depends(oauth2.get_current_user)):
  job = db.query(models.Job).filter(models.Job.Id == id).first()

  if job == None:
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                        detail=f"Job with id: ({id}) does not exist")
  
  if job.user_id == current_user.id:
    raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, 
                        detail=f"Not authorized to perform the requested action")

  job.update(updated_job.dict(), Synchronize_seasion= False)
  db.commit()
  return job


  







