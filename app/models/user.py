from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum
import database

class UserRole(str, enum.Enum):
    CANDIDATE = "candidate"
    HR = "hr"


class UserModel(database.Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(50))
    email = Column(String(50), unique=True, index=True)
    password = Column(String(50))
    date_of_birth = Column(DateTime(timezone=True), default=func.now())
    role = Column(Enum(UserRole))
    phone = Column(String(10))