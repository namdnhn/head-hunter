from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import database

class Job(database.Base):
    __tablename__ = "job"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("company.id"))
    position = Column(String(250))
    description = Column(String(250))
    posting_date = Column(DateTime(timezone=True), default=func.now())
    deadline = Column(DateTime(timezone=True), default=func.now())
    location = Column(String(250))
    job_requirement = Column(String(250))
    Salary = Column(Integer)
    job_status = Column(Boolean)

    company = relationship("Company", back_populates="job_company")
    post = relationship("Post", back_populates="job_post")
    application_job = relationship("Application", back_populates="job_application")
