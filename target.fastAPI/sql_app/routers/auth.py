from fastapi import Depends, status, HTTPException, APIRouter
from http.client import HTTPException
from sqlalchemy.orm import Session
from .. import database, schema, crud, utils, oauth2
from .. import models

router =APIRouter(
  prefix="/auth",
  tags=["authentication"]
)

@router.post('/login')
def login(user_credntials:schema.UserLogin, db: Session= Depends(database.get_db)):
  db_user = crud.get_user_by_email(db, email = user_credntials.email)
  if not db_user:
    raise HTTPException(status_code =status.HTTP_403_FORBIDDEN,
                        detial=f"invalid credentials")
                        
  if not utils.verify(user_credntials.password, db_user.password):
    raise HTTPException(status_code =status.HTTP_403_FORBIDDEN,
                        detial=f"invalid credentials")
  
  access_token = oauth2.create_access_token(data= {"user_id":db_user.id})
  return {"token":access_token, "token_type":"bearer"}