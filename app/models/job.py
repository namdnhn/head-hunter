import enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import database

class LevelJob(str, enum.Enum):
    INTERN = "intern"
    FRESHER = "fresher"
    JUNIOR = "junior"

class JobModel(database.Base):
    __tablename__ = "job"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("company.id"))
    quantity = Column(Integer)
    level = Column(Enum(LevelJob))
    role = Column(String(250))
    address = Column(String(250))
    skills = Column(String(250))
    description = Column(String(250))
    demand = Column(String(250))
    posting_date = Column(DateTime(timezone=True), default=func.now())
    deadline = Column(DateTime(timezone=True), default=func.now())
    salary = Column(Integer)
    benefit = Column(String(250))
    job_status = Column(Boolean)
    urgent = Column(Boolean)

    company = relationship("CompanyModel")
    post = relationship("PostModel")
