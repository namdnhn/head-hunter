from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import database
from .job import JobModel

class PostModel(database.Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("job.id"))
    title = Column(String(50))
    content = Column(String(300))

    job_post = relationship("JobModel")
