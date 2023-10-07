from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import database


class Company(database.Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    description = Column(String(300))

    job_company = relationship("Job", back_populates="company")
