from typing import Optional
from pydantic import BaseModel


class CreateCv(BaseModel):
    user_id: int
    experience: str
    position: str
    skill: str
    education: str
    achivement: str
    activity: str

    class Config:
        orm_mode = True


class UpdateCv(CreateCv):
    user_id: Optional[int]
    experience: Optional[str]
    position: Optional[str]
    skill: Optional[str]
    education: Optional[str]
    achivement: Optional[str]
    activity: Optional[str]
