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