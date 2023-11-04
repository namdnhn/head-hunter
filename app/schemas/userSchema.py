from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# class UserRole(str, Enum):
#     CANDIDATE = "candidate"
#     HR = "hr"


class Login(BaseModel):
    email: str
    password: str


class RegisterUser(Login):
    fullname: str
    date_of_birth: datetime
    # role: UserRole
    phone: str

    class Config:
        orm_mode = True


class ConfirmPassword(BaseModel):
    currentPass: str


class UpdateUser(ConfirmPassword):
    email: Optional[str] = None
    newPassword: Optional[str] = None
    fullname: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    # role: Optional[UserRole] = None
    phone: Optional[str] = None
