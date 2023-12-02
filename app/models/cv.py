from sqlalchemy import ARRAY, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class CvModel(Base):
    __tablename__ = "cv"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    image_path = Column(String(100))
    pdf_path = Column(String(100))
    location = Column(String(100))
    position = Column(String(300))
    skill = Column(String(300))
    degree = Column(String(300))
    achivement = Column(String(300))
    activity = Column(String(300))
    language = Column(String(300))

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
