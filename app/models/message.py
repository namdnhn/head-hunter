from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import database
import enum

class MessageType(str, enum.Enum):
    TEXT = "text"
    IMAGE = "image"
    FILE = "file"

class MessageModel(database.Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True, index=True)
    send_at = Column(DateTime(timezone=True), default=func.now())
    conversation_id = Column(Integer, ForeignKey("conversation.id"))
    sender_id = Column(Integer, ForeignKey("user.id"))
    file_id = Column(Integer, ForeignKey("file.id"))
    msg_text = Column(Text)
    msg_type = Column(Enum(MessageType))
    
    sender = relationship("UserModel")
    conversation = relationship("ConversationModel")
    file = relationship("FileModel")