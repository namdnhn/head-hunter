from fastapi import APIRouter, Depends
from controllers.jobController import JobController
from schemas.jobSchema import JobCreate, UpdateJob
from sqlalchemy.orm import Session
from database import getDatabase


router = APIRouter(
    prefix="/job",
    tags=["job"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def createJob(request: JobCreate, db: Session=Depends(getDatabase)):
    # print("go here")
    return JobController.createJob(request=request, db=db)

@router.get("/job/{jobId}")
def getJobById(jobId: int, db: Session=Depends(getDatabase)):
    return JobController.getJobById(jobId=jobId, db=db)

@router.put("/job/update/{jobId}")
def updateJob(jobId: int, job: UpdateJob, db: Session = Depends(getDatabase)):
    return JobController.updateJob(jobId=jobId, job=job, db=db)

@router.delete("/job/delete/{jobId}")
def deleteJob(jobId: int, db: Session = Depends(getDatabase)):
    return JobController.deleteJob(jobId=jobId, db=db)