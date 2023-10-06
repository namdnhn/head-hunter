from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base


class Job(Base):
    __tablename__ = "job"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("company.id"))
    position = Column(String)
    description = Column(String)
    posting_date = Column(DateTime(timezone=True), default=func.now())
    deadline = Column(DateTime(timezone=True), default=func.now())
    location = Column(String)
    job_requirement = Column(String)
    Salary = Column(Integer)
    job_status = Column(Boolean)

    company = relationship("Company", back_populates="job")
    post = relationship("Post", back_populates="job")
    application = relationship("Application", back_populates="job")
