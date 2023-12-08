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
    level = Column(Enum(LevelJob))
    role = Column(String(250))
    require = Column(Text)
    job_detail = Column(Text)
    degree_skill = Column(Text)
    salary = Column(String(250))
    benefit = Column(Text)
    urgent = Column(Boolean)
    featured = Column(Boolean)
    company_name = Column(String(250))
    company_logo = Column(String(250))
    quantity = Column(Integer)
    address = Column(String(250))
    description = Column(Text)
    posting_date = Column(DateTime(timezone=True), default=func.now())
    deadline = Column(DateTime(timezone=True), default=func.now())
    urgent = Column(Boolean)

    company = relationship("CompanyModel")
    post = relationship("PostModel")
