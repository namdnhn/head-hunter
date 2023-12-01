from typing import Optional
from pydantic import BaseModel
from models.job import LevelJob
from datetime import datetime

class CreateJob(BaseModel):
    company_id: int
    quantity: int
    level: LevelJob
    role: str
    address: str
    skills: str
    description: str
    demand: str
    posting_date: datetime
    deadline: datetime
    salary: int
    benefit: str
    job_status: bool
    urgent: bool
    class Config:
        orm_mode = True


class UpdateJob(CreateJob):
    company_id: Optional[int]
    quantity: Optional[int]
    level: Optional[LevelJob]
    role: Optional[str]
    address: Optional[str]
    skills: Optional[str]
    description: Optional[str]
    demand: Optional[str]
    posting_date: Optional[datetime]
    deadline: Optional[datetime]
    salary: Optional[int]
    benefit: Optional[str]
    job_status: Optional[bool]
    urgent: Optional[bool]
