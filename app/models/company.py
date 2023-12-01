from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import database


class CompanyModel(database.Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, index=True)
    job_quantity = Column(Integer)
    name = Column(String(50), index=True)
    address = Column(String(300))
    founded_year = Column(Integer)
    employee_quantity = Column(Integer)
    description = Column(String(300))
    contact = Column(String(50))