from typing import Optional
from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from controllers.jobController import JobController
from database import getDatabase
from schemas.jobSchema import CreateJob, UpdateJob

router = APIRouter(
    prefix="/job",
    tags=["Job"],
    responses={404: {"description": "Not found"}},
)

@router.get("") 
def get_all_job_available(page: int = 1, size: int = 10, db: Session = Depends(getDatabase)):
    return JobController.getAllJobAvailable(page=page, size=size, db=db)

@router.get("/{jobId}")
def get_job_by_job_id(jobId: int, db: Session = Depends(getDatabase)):
    return JobController.getJobByJobId(jobId=jobId, db=db)


@router.get("/company/{companyId}")
def get_job_by_company_id(companyId: int, db: Session = Depends(getDatabase)):
    return JobController.getJobByCompanyId(companyId=companyId, db=db)


@router.post("/create")
def create_job(job: CreateJob = Depends(), db: Session = Depends(getDatabase)
):
    return JobController.createJob(job=job, db=db)


@router.put("/update/{jobId}")
def update_job(
    jobId: int,
    job: UpdateJob = Depends(),
    db: Session = Depends(getDatabase),
):
    return JobController.updateJob(jobId=jobId, job=job, db=db)


@router.delete("/delete/{jobId}")
def delete_cv(
    jobId: int,
    db: Session = Depends(getDatabase),
):
    return JobController.deleteJob(jobId=jobId, db=db)
