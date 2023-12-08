from typing import Optional
from schemas.jobSchema import CreateJob, UpdateJob
from models.job import JobModel
from sqlalchemy.orm import Session
from fastapi import Depends
from database import getDatabase
from datetime import datetime



class JobController:
    def createJob(
        job: CreateJob,
        db: Session = Depends(getDatabase),
    ):
        db_job = JobModel(
            company_id=job.company_id,
            level=job.level,
            role=job.role,
            require=job.require,
            job_detail=job.job_detail,
            degree_skill=job.degree_skill,
            salary=job.salary,
            benefit=job.benefit,
            urgent=job.urgent,
            featured=job.featured,
            company_name=job.company_name,
            company_logo=job.company_logo,
            quantity=job.quantity,
            address=job.address,
            description=job.description,
            posting_date=job.posting_date,
            deadline=job.deadline,
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
        skip = (page - 1) * size
        # return db.query(JobModel).filter(JobModel.deadline < datetime.now()).offset(skip).limit(size).all()
        return db.query(JobModel).offset(skip).limit(size).all()
    

    def updateJob(
        jobId: int,
        job: UpdateJob,
        db: Session = Depends(getDatabase),
    ):
        dbJob = db.query(JobModel).filter(JobModel.id == jobId).first()
        if job.company_id is not None:
            dbJob.company_id = job.company_id
        if job.level is not None:
            dbJob.level = job.level
        if job.role is not None:
            dbJob.role = job.role
        if job.require is not None:
            dbJob.require = job.require
        if job.job_detail is not None:
            dbJob.job_detail = job.job_detail
        if job.degree_skill is not None:
            dbJob.degree_skill = job.degree_skill
        if job.salary is not None:
            dbJob.salary = job.salary
        if job.benefit is not None:
            dbJob.benefit = job.benefit
        if job.urgent is not None:
            dbJob.urgent = job.urgent
        if job.featured is not None:
            dbJob.featured = job.featured
        if job.company_name is not None:
            dbJob.company_name = job.company_name
        if job.company_logo is not None:
            dbJob.company_logo = job.company_logo
        if job.quantity is not None:
            dbJob.quantity = job.quantity
        if job.address is not None:
            dbJob.address = job.address
        if job.description is not None:
            dbJob.description = job.description
        if job.posting_date is not None:
            dbJob.posting_date = job.posting_date
        if job.deadline is not None:
            dbJob.deadline = job.deadline
        db.commit()
        return {"msg": "Updated!"}

    def deleteJob(jobId: int, db: Session = Depends(getDatabase)):
        dbJob = db.query(JobModel).filter(JobModel.id == jobId).first()
        db.delete(dbJob)
        db.commit()
        return {"msg": "Deleted!"}
