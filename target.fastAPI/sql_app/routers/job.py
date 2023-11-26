from fastapi import Depends, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .. import models, schema, database, oauth2

router = APIRouter(
  prefix = "/jobs",
  tags = ["Jobs"]
)

@router.post("/", status_code = status.HTTP_201_CREATED, 
             response_model = schema.JobOutput)
def create_job(job: schema.JobCreate, db: Session=Depends(database.get_db),
          current_user: int = Depends(oauth2.get_current_user)):
  
  new_job= models.Job(user_id = current_user.id, **job.model_dump())
  db.add(new_job)
  db.commit()
  db.refresh(new_job)
  return new_job


@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_job(id: int, db: Session = Depends(database.get_db), 
                current_user: int = Depends(oauth2.get_current_user)):
  job_query = db.query(models.Job).filter(models.Job.id == id)
  job = job_query.first()
  if job == None:
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                        detail = f"Job with id: ({id}) does not exist")
  
  if job.user_id != current_user.id:
    raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, 
                        detail = "Not authorized to perform the requested action")

  job_query.delete(synchronize_session = False)
  db.commit()
  return Response(status_code = status.HTTP_202_ACCEPTED)


@router.put("/{id}", status_code = status.HTTP_201_CREATED, response_model = schema.JobOutput)
def update_job(id:int, updated_job: schema.JobCreate, db: Session = Depends(database.get_db),
          current_user: int = Depends(oauth2.get_current_user)):
  job_query = db.query(models.Job).filter(models.Job.id == id and models.Job.user_id == current_user.id)
  job = job_query.first()
  print(f"SQL_QUERY:: {job}")
  if job == None:
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                        detail = f"Job with id: ({id}) does not exist")
  
  if job.user_id != current_user.id:
    raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, 
                        detail = "Not authorized to perform the requested action")

  job_query.update(updated_job.model_dump(), synchronize_session= False)
  db.commit()
  return job_query.first()


  







