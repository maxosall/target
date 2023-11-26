from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .. import crud, schema, database, oauth2, models

router =APIRouter(
  prefix="/users",
  tags=["Users"]
)


@router.get("/", response_model=list[schema.UserOutput])
async def read_users(db: Session = Depends(database.get_db)):
  users = crud.get_users(db)
  return  users


@router.get("/{user_id}", response_model=schema.UserOutput)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
  db_user = crud.get_user(db, user_id=user_id)
  if db_user is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id:({user_id}) not found")
  return db_user


@router.post("/", status_code = status.HTTP_201_CREATED, 
          response_model=schema.UserOutput)
def create_user(user: schema.UserCreate, db: Session = Depends(database.get_db)):
  new_user = crud.get_user_by_email(db, email=user.email)
  if new_user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email already registered")
  return crud.create_user(db=db, user=user)


@router.post("/profile", status_code= status.HTTP_201_CREATED,
             response_model=schema.ProfileOutput)
def create_profile(profile: schema.ProfileCreate, db: Session = Depends(database.get_db),
                   current_user: int= Depends(oauth2.get_current_user)):   
  
  user_profile = db.query(models.Profile).filter(models.Profile.user_id == current_user.id).first()
  
  # if current_user already have a profile
  if user_profile:
    raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, 
                        detail = "Not authorized to create another profile, you already has one")
  
  # if current_user has not has a profile yet
  new_user_profile = models.Profile(user_id = current_user.id, **profile.model_dump())
  db.add(new_user_profile)
  db.commit()
  db.refresh(new_user_profile)
  return new_user_profile



@router.get("/profile/{profile_id}", response_model=schema.ProfileDetails)
async def read_profile(profile_id: int, db: Session = Depends(database.get_db), 
                 current_user: int = Depends(oauth2.get_current_user)):
  profile = db.query(models.Profile).filter(models.Profile.id == profile_id 
                                            and models.Profile.user_id == current_user.id).first()

  if not profile:
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                        detail = f"Profile with id ({profile_id}) does not exist.")
  
  if profile.user_id != current_user.id:
    raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, 
                        detail = "Not authorized to perform the requested action")
  return profile


