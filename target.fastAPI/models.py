from dataclasses import Field
from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from pytdantic import BaseModel


class Job(BaseModel):
  id: Optional[UUID] = uuid4
  title: str
  description: str
  min_salary: float
  max_salary: float

  added_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
  modified_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
  openning_date: datetime.datetime = added_at
  closing_date: datetime.datetime

class JobType(str, Enum):
  full_time: "full time" 
  part_time: 'part time'
  contractor: 
class application(BasedModel):
  pass