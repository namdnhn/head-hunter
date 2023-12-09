from datetime import datetime
from pydantic import BaseModel

class ConversationCreate(BaseModel):
    created_id: int
    name: str

class Conversation(ConversationCreate):
    id: int
    members: int
    
    class Config:
        orm_mode = True
    
class MessageCreate(BaseModel):
    sender_id: int
    conversation_id: int
    content: str
    
class Message(MessageCreate):
    id: int
    timestamp: datetime
    
    class Config:
        orm_mode = True