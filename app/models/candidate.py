from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import database



class CandidateModel(database.Base):
    __tablename__ = "candidate"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    cv_id = Column(Integer, ForeignKey("cv.id"))