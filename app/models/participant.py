from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import database
import enum

class ParticipantModel(database.Base):
    __tablename__ = "participant"
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversation.id"))
    sender_id = Column(Integer, ForeignKey("user.id"))
    joined_at = Column(DateTime(timezone=True), default=func.now())
    
    user = relationship("UserModel")
    conversation = relationship("ConversationModel")