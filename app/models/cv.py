from sqlalchemy import ARRAY, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.sqltypes import Text

class CvModel(Base):
    __tablename__ = "cv"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    introduce = Column(String(1000))
    email = Column(String(100))
    phone = Column(String(100))
    gender = Column(String(100))
    date_of_birth = Column(DateTime(timezone=True), default=func.now())
    role = Column(String(100))
    year_experience = Column(String(100))
    degree = Column(String(100))
    current_address = Column(String(100))
    skill = Column(Text)
    language = Column(Text)
    cv = Column(String(300))
    avatar = Column(String(300))

    # Define relationships to Experience and Education
    experiences = relationship("Experience", back_populates="cv")
    educations = relationship("Education", back_populates="cv")

class Experience(Base):
    __tablename__ = "experience"
    id = Column(Integer, primary_key=True, index=True)
    cv_id = Column(Integer, ForeignKey("cv.id"))
    company = Column(String(100))
    time = Column(String(100))
    # position = Column(String(100))

    # Define the relationship to CvModel
    cv = relationship("CvModel", back_populates="experiences")

class Education(Base):
    __tablename__ = "education"
    id = Column(Integer, primary_key=True, index=True)
    cv_id = Column(Integer, ForeignKey("cv.id"))
    school = Column(String(100))
    time = Column(String(100))
    department = Column(String(100))

    # Define the relationship to CvModel
    cv = relationship("CvModel", back_populates="educations")
