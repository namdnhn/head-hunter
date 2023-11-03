from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum
from schemas.userSchema import User
from schemas.fileSchema import File
from models.message import MessageType

class MessageCreate(BaseModel):
    conversation_id: int
    sender_id: int
    file_id: Optional[int]
    msg_text: str
    msg_type: MessageType
    
class Message(MessageCreate):
    id: int
    send_at: datetime
    
    file: Optional[File]
    class Config:
        orm_mode=True
    
class ConversationCreate(BaseModel):
    name: Optional[str]
    created_by: Optional[int]
    
class Conversation(ConversationCreate):
    id: int
    created_at: datetime
    created_by_user: Optional[User]
    messages: Optional[list[Message]]
    
    class Config:
        orm_mode = True
        
class ParticipantCreate(BaseModel):
    conversation_id: int
    sender_id: int
    
class Participant(ParticipantCreate):
    id: int
    joined_at: datetime
    
    conversation: Conversation
    class Config:
        orm_mode=True
        


