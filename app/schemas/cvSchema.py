from typing import Optional
from pydantic import BaseModel


class CreateCv(BaseModel):
    user_id: int
    image_path: str
    pdf_path: str
    location: str
    # experience: str
    # education: str
    degree: str
    position: str
    skill: str
    achivement: str
    activity: str
    language: str

    class Config:
        orm_mode = True


class UpdateCv(CreateCv):
    user_id: Optional[int]
    image_path: Optional[str]
    pdf_path: str
    location: Optional[str]
    experience: Optional[str]
    education: Optional[str]
    degree: Optional[str]
    position: Optional[str]
    skill: Optional[str]
    achivement: Optional[str]
    activity: Optional[str]
    language: Optional[str]
