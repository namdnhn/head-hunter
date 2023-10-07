from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base


class Cv(Base):
    __tablename__ = "cv"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    image_path = Column(String)
    experience = Column(String)
    position = Column(String)
    skill = Column(String)
    education = Column(String)
    achivement = Column(String)
    activity = Column(String)

    owner = relationship("User", back_populates="cv")
    application = relationship("Application", back_populates="cv")
