from fastapi import APIRouter, Depends, Response
from schemas.candidateSchema import CandidateCreate, CandidateUpdate
from controllers.candidateController import candidateController
from sqlalchemy.orm import Session
from database import getDatabase


router = APIRouter(
    prefix="/candidate",
    tags=["candidate"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def createCandidate(request: CandidateCreate, db: Session=Depends(getDatabase)):
    # print("go here")
    return candidateController.createCandidate(request=request, db=db)

@router.get("/candidate/{candidateId}")
def getcandidateById(candidateId: int, db: Session=Depends(getDatabase)):
    return candidateController.getcandidateById(candidateId=candidateId, db=db)

@router.get("/candidate/info/{candidate_id}")
def getcandidateInfo(candidate_id: int, db: Session=Depends(getDatabase)):
    return candidateController.getCandidateInfo(candidate_id=candidate_id, db=db)

@router.put("/candidate/update/{candidateId}")
def updatecandidate(candidateId: int, candidate: CandidateUpdate, db: Session = Depends(getDatabase)):
    return candidateController.updateCandidate(candidateId=candidateId, candidate=candidate, db=db)

@router.delete("/candidate/delete/{candidateId}")
def deletecandidate(candidateId: int, db: Session = Depends(getDatabase)):
    return candidateController.deleteCandidate(candidateId=candidateId, db=db)