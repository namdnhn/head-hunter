from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import database


class ConversationModel(database.Base):
    __tablename__ = "conversation"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    created_by = Column(Integer, ForeignKey("user.id"))
    
    created_by_user = relationship("UserModel")
    messages = relationship("MessageModel")