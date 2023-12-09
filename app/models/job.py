import enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import Text
import database


class LevelJob(str, enum.Enum):
    INTERN = "intern"
    FRESHER = "fresher"
    JUNIOR = "junior"
    MIDDLE = "middle"
    SENIOR = "senior"
    LEAD = "lead"
    MANAGER = "manager"
    DIRECTOR = "director"
    CTO = "cto"
    CEO = "ceo"


class JobModel(database.Base):
    __tablename__ = "job"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("company.id"))
    level = Column(Text)
    role = Column(Text)
    require = Column(Text)
    job_detail = Column(Text)
    degree_skill = Column(Text)
    salary = Column(Text)
    benefit = Column(Text)
    urgent = Column(Boolean)
    featured = Column(Boolean)
    company_name = Column(Text)
    company_logo = Column(Text)
    quantity = Column(Text)
    address = Column(Text)
    description = Column(Text)
    demand = Column(Text)
    posting_date = Column(DateTime(timezone=True), default=func.now())
    deadline = Column(DateTime(timezone=True), default=func.now())

    company = relationship("CompanyModel")
    post = relationship("PostModel")
