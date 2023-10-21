from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum
from schemas.userSchema import User
from schemas.fileSchema import File
from models.message import MessageType

class ConversationCreate(BaseModel):
    name: str
    created_by: int
    
class Conversation(ConversationCreate):
    id: int
    created_at: datetime
    created_by_user: User
    
    class Config:
        orm_mode = True
        
class ParticipantCreate(BaseModel):
    conversation_id: int
    sender_id: int
    
class Participant(ParticipantCreate):
    id: int
    joined_at: datetime
    
    user: User
    conversation: Conversation
    class Config:
        orm_mode=True
        
class MessageCreate(BaseModel):
    conversation_id: int
    sender_id: int
    file_id: int
    msg_text: str
    msg_type: MessageType
    
class Message(MessageCreate):
    id: int
    send_at: datetime
    
    sender: User
    conversation: Conversation
    file: File

