from pydantic import BaseModel

class CompanyCreate(BaseModel):
    job_quantity: int
    name: str
    address: str
    founded_year: int
    employee_quantity: int
    description: str
    description: str
    contact: str

class Company(CompanyCreate):
    id: int
    class Config:
        orm_mode = True