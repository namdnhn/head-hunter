from pydantic import BaseModel
from typing import Optional

class CompanyCreate(BaseModel):
    user_id: int
    job_quantity: int
    name: str
    address: str
    founded_year: int
    employee_quantity: int
    description: str
    description: str
    contact: str
    logo: str

class Company(CompanyCreate):
    id: int
    class Config:
        orm_mode = True

class CompanyUpdate(BaseModel):
    user_id: Optional[int] = None
    job_quantity: Optional[int] = None
    name: Optional[str] = None
    address: Optional[str] = None
    founded_year: Optional[int] = None
    employee_quantity: Optional[int] = None
    description: Optional[str] = None
    contact: Optional[str] = None
    logo: Optional[str] = None