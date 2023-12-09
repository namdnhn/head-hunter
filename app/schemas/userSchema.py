from enum import Enum
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserRole(str, Enum):
    CANDIDATE = "candidate"
    HR = "hr"

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class Login(BaseModel):
    email: str
    password: str


class RegisterUser(BaseModel):
    fullname: str
    image_path: str
    email: str
    password: str
    date_of_birth: datetime
    gender: Gender
    role: UserRole
    phone: str

    class Config:
        orm_mode = True


class ConfirmPassword(BaseModel):
    currentPass: str


class UpdateUser(ConfirmPassword):
    fullname: Optional[str] = None
    email: Optional[str] = None
    newPassword: Optional[str] = None
    fullname: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    # role: Optional[UserRole] = None
    phone: Optional[str] = None

class UpdateUser2(BaseModel):
    fullname: Optional[str] = None
    image_path: Optional[str] = None
    email: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    gender: Optional[Gender] = None
    role: Optional[UserRole] = None
    phone: Optional[str] = None
