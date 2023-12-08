from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class CreateCv(BaseModel):
    user_id: int
    introduce: str
    email: str
    phone: str
    gender: str
    date_of_birth: datetime
    role: str
    year_experience: str
    degree: str
    current_address: str
    skill: str
    language: str
    cv: str
    avatar: str

    class Config:
        orm_mode = True


class UpdateCv(CreateCv):
    user_id: Optional[int]
    introduce: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    gender: Optional[str]
    date_of_birth: Optional[datetime]
    role: Optional[str]
    year_experience: Optional[str]
    degree: Optional[str]
    current_address: Optional[str]
    skill: Optional[str]
    language: Optional[str]
    cv: Optional[str]
    avatar: Optional[str]
