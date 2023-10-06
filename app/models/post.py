from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("job.id"))
    title = Column(String)
    content = Column(String)

    job = relationship("Job", back_populates="post")
