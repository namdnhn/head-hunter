from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import database
from .user import UserModel

class CvModel(database.Base):
    __tablename__ = "cv"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    image_path = Column(String(100))
    experience = Column(String(300))
    position = Column(String(300))
    skill = Column(String(300))
    education = Column(String(300))
    achivement = Column(String(300))
    activity = Column(String(300))

    owner = relationship("UserModel")