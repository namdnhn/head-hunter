from typing import Optional
from pydantic import BaseModel
from models.job import LevelJob
from datetime import datetime

class CreateJob(BaseModel):
    company_id: int
    level: LevelJob
    role: str
    require: str
    job_detail: str
    degree_skill: str
    salary: str
    benefit: str
    urgent: bool
    featured: bool
    company_name: str
    company_logo: str
    quantity: int
    address: str
    description: str
    posting_date: datetime
    deadline: datetime
    class Config:
        orm_mode = True


class UpdateJob(CreateJob):
    company_id: Optional[int]
    level: Optional[LevelJob]
    role: Optional[str]
    require: Optional[str]
    job_detail: Optional[str]
    degree_skill: Optional[str]
    salary: Optional[str]
    benefit: Optional[str]
    urgent: Optional[bool]
    featured: Optional[bool]
    company_name: Optional[str]
    company_logo: Optional[str]
    quantity: Optional[int]
    address: Optional[str]
    description: Optional[str]
    posting_date: Optional[datetime]
    deadline: Optional[datetime]
