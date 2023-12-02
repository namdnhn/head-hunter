from pydantic import BaseModel
from typing import Optional

class CandidateCreate(BaseModel):
    user_id: int
    cv_id: int

# class Hr(HrCreate):
#     id: int
#     class Config:
#         orm_mode = True

class CandidateUpdate(BaseModel):
    user_id: int
    cv_id: int
    # user_id: Optional[int] = None
    # company_id: Optional[int] = None
    