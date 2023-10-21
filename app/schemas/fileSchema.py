from pydantic import BaseModel
from datetime import datetime
from models.file import FileType

class FileCreate(BaseModel):
    file_name: str
    file_path: str
    file_size: int
    file_type: FileType
    created_by: int
    
class File(FileCreate):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True