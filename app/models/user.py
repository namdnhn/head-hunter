from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum
from datetime import datetime
import database

class UserRole(str, enum.Enum):
    CANDIDATE = "candidate"
    HR = "hr"

class Gender(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"


class UserModel(database.Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(50))
    image_path = Column(String(100))
    email = Column(String(50), unique=True, index=True)
    password = Column(String(300))
    date_of_birth = Column(DateTime(timezone=True), default=func.now())
    gender = Column(Enum(Gender))
    role = Column(Enum(UserRole), default=UserRole.CANDIDATE)
    phone = Column(String(10))