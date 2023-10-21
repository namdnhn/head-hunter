from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import database
import enum

class FileType(str, enum.Enum):
    IMG = "image"
    MP3 = "mp3"
    VID = "video"
    OTHER = "other"

class FileModel(database.Base):
    __tablename__ = "file"
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(50), index=True)
    file_path = Column(String(200))
    file_size = Column(Integer)
    file_type = Column(Enum(FileType))
    created_at = Column(DateTime(timezone=True), default=func.now())
    created_by = Column(Integer, ForeignKey("user.id"))
    
    created_by_user = relationship("UserModel")