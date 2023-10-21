from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.sql import func
import database

class HrModel(database.Base):
    __tablename__ = "hr"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), unique=True)
    company_id = Column(Integer, ForeignKey("company.id"))
