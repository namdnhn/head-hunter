from fastapi import Depends, HTTPException
from models.company import CompanyModel
from models.job import JobModel
from schemas.jobSchema import JobCreate, UpdateJob
from database import getDatabase
from sqlalchemy.orm import Session


class JobController:
    @staticmethod
    def createJob(request: JobCreate, db: Session):
        newJob = JobModel(
            company_id = request.company_id,
            position = request.position,
            description = request.description,
            posting_date = request.posting_date,
            deadline = request.deadline,
            location = request.location,
            job_requirement = request.job_requirement,
            salary = request.salary,
            job_status = request.job_status,
        )
        db.add(newJob)
        db.commit()
        db.refresh(newJob)
        return newJob
    
    def getJobById(jobId: int, db: Session = Depends(getDatabase)):
        return db.query(JobModel).filter(JobModel.id == jobId).first()

    def updateJob(jobId: int, job: UpdateJob, db: Session):
        dbJobId = db.query(JobModel).filter(JobModel.id == jobId).first()
        if job.company_id is not None:
            # Check if company_id exists in the database
            company = db.query(CompanyModel).filter(CompanyModel.id == job.company_id).first()
            if company is not None:
                dbJobId.company_id = job.company_id
            else:
                raise HTTPException(status_code=400, detail="Invalid company_id")
        dbJobId.position = job.position
        dbJobId.description = job.description
        dbJobId.posting_date = job.posting_date
        dbJobId.deadline = job.deadline
        dbJobId.location = job.location
        dbJobId.job_requirement = job.job_requirement
        dbJobId.salary = dbJobId.salary
        dbJobId.job_status = dbJobId.job_status

        db.commit()
        return {"msg": "Updated"}
    
    def deleteJob(jobId: int, db: Session):
        dbJobId = db.query(JobModel).filter(JobModel.id == jobId).first()
        db.delete(dbJobId)
        db.commit()
        return {"msg": "Deleted"}
    
