from sqlalchemy import Boolean, Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import database

class Application(database.Base):
    __tablename__ = "application"
    id = Column(Integer, primary_key=True, index=True)
    cv_id = Column(Integer, ForeignKey("cv.id"))
    job_id = Column(Integer, ForeignKey("job.id"))
    application_date = Column(DateTime(timezone=True), default=func.now())
    application_status = Column(Boolean)

    cv_application = relationship("Cv", back_populates="application_cv")
    job_application = relationship("Job", back_populates="application_job")
