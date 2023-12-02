from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from typing import List


class Education(BaseModel):
    school: str
    time: datetime
    department: str
    degree: str

class Experience(BaseModel):
    company: str
    time: datetime
    position: str

class CvCreate(BaseModel):
    user_id: int
    image_path: str
    location: str
    experiences: List[Experience]
    position: str
    skill: str
    educations: List[Education] 
    achivement: str
    activity: str
    language: str

# class Hr(HrCreate):
#     id: int
#     class Config:
#         orm_mode = True

# class UpdateHr(BaseModel):
#     user_id: Optional[int] = None
#     company_id: Optional[int] = None