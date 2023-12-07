from typing import Optional
from schemas.jobSchema import CreateJob, UpdateJob
from models.job import JobModel
from sqlalchemy.orm import Session
from fastapi import Depends
from database import getDatabase
from datetime import datetime



class JobController:
    def createJob(
        job: CreateJob = Depends(),
        db: Session = Depends(getDatabase),
    ):
        db_job = JobModel(
            company_id=job.company_id,
            quantity=job.quantity,
            level=job.level,
            role=job.role,
            address=job.address,
            skills=job.skills,
            description=job.description,
            demand=job.demand,
            posting_date=job.posting_date,
            deadline=job.deadline,
            salary=job.salary,
            benefit=job.benefit,
            job_status=job.job_status,
            urgent=job.urgent,
        )
        db.add(db_job)
        db.commit()
        db.refresh(db_job)
        return db_job

    def getJobByJobId(jobId: int, db: Session = Depends(getDatabase)):
        return db.query(JobModel).filter(JobModel.id == jobId).first()

    def getJobByCompanyId(companyId: int, db: Session = Depends(getDatabase)):
        return db.query(JobModel).filter(JobModel.company_id == companyId).all()
    
    def getAllJobAvailable(page: int = 1, size: int = 10, db: Session = Depends(getDatabase)):
        skip = page * size
        return db.query(JobModel).filter(JobModel.deadline < datetime.now()).offset(skip).limit(size).all()

    def updateJob(
        jobId: int,
        job: UpdateJob,
        db: Session = Depends(getDatabase),
    ):
        dbJob = db.query(JobModel).filter(JobModel.id == jobId).first()
        if job.company_id is not None:
            dbJob.company_id = job.company_id
        if job.quantity is not None:
            dbJob.quantity = job.quantity
        if job.level is not None:
            dbJob.level = job.level
        if job.role is not None:
            dbJob.role = job.role
        if job.address is not None:
            dbJob.address = job.address
        if job.skills is not None:
            dbJob.skills = job.skills
        if job.description is not None:
            dbJob.description = job.description
        if job.demand is not None:
            dbJob.demand = job.demand
        if job.posting_date is not None:
            dbJob.posting_date = job.posting_date
        if job.deadline is not None:
            dbJob.deadline = job.deadline
        if job.salary is not None:
            dbJob.salary = job.salary
        if job.benefit is not None:
            dbJob.benefit = job.benefit
        if job.job_status is not None:
            dbJob.job_status = job.job_status
        if job.urgent is not None:
            dbJob.urgent = job.urgent
        db.commit()
        return {"msg": "Updated!"}

    def deleteJob(jobId: int, db: Session = Depends(getDatabase)):
        dbJob = db.query(JobModel).filter(JobModel.id == jobId).first()
        db.delete(dbJob)
        db.commit()
        return {"msg": "Deleted!"}
