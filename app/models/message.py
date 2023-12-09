from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import database

class ConversationModel(database.Base):
    __tablename__ = "conversation"
    id = Column(Integer, primary_key=True, index=True)
    created_id = Column(Integer, ForeignKey("user.id"))
    name = Column(String(255), default="")
    members = Column(Integer, default=2)
    
    conversation_user = relationship("UserModel")
    
class ConversationMemberModel(database.Base):
    __tablename__ = "conversation_member"
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversation.id"))
    member_id = Column(Integer, ForeignKey("user.id"))
    
    conversation_member = relationship("ConversationModel")
    member_member = relationship("UserModel")
    
class MessageModel(database.Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("user.id"))
    conversation_id = Column(Integer, ForeignKey("conversation.id"))
    content = Column(String(255), nullable=False)
    timestamp = Column(DateTime, default=func.now())

    sender_user = relationship("UserModel")
    conversation_conversation = relationship("ConversationModel")