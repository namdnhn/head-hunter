from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from enum import Enum
from ..database import Base


class UserRole(str, Enum):
    CANDIDATE = "candidate"
    HR = "hr"


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    date_of_birth = Column(DateTime(timezone=True), default=func.now())
    role = Column(UserRole)
    phone = Column(String(10))

    cv = relationship("Cv", back_populates="owner")
