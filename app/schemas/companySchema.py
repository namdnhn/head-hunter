from pydantic import BaseModel

class CompanyCreate(BaseModel):
    name: str
    description: str

class Company(CompanyCreate):
    id: int
    class Config:
        orm_mode = True