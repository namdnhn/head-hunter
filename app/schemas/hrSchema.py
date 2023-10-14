from pydantic import BaseModel
from typing import Optional

class HrCreate(BaseModel):
    user_id: int
    company_id: int

class Hr(HrCreate):
    id: int
    class Config:
        orm_mode = True

class UpdateHr(BaseModel):
    user_id: Optional[int] = None
    company_id: Optional[int] = None