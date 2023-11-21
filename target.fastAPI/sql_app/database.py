from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator
# from . config import get_settings


# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# settings = get_settings()

SQLALCHEMY_DATABASE_URL = 'sqlite:///./target.db'
engine = create_engine(
  SQLALCHEMY_DATABASE_URL,
  # get_settings().DATABASE_URL, 
  # pool_pre_ping= True,
  # pool_recycle=300,
  
  pool_size=10, 
  max_overflow=20,
  connect_args= {'check_same_thread':False}
)

SessionLocal = sessionmaker(autocommit = False ,autoflush= False, bind= engine)

Base = declarative_base()