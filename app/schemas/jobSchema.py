from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from models.company import CompanyModel
from models.post import PostModel

class JobCreate(BaseModel):
    company_id: int
    position: str
    description: str
    posting_date: datetime
    deadline: datetime
    location: str
    job_requirement: str
    salary: int
    job_status: bool

class Job(JobCreate):
    id: int
    class Config:
        orm_mode = True

class UpdateJob(BaseModel):
    company_id: Optional[int] = None
    position: Optional[str] = None
    description: Optional[str] = None
    posting_date: Optional[datetime] = None
    deadline: Optional[datetime] = None
    location: Optional[str] = None
    job_requirement: Optional[str] = None
    salary: Optional[int] = None
    job_status: Optional[bool] = None