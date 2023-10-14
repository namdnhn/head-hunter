from fastapi import APIRouter, Depends, Response
from controllers.hrController import HrController
from schemas.hrSchema import HrCreate, UpdateHr
from sqlalchemy.orm import Session
from database import getDatabase


router = APIRouter(
    prefix="/hr",
    tags=["hr"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def createHr(request: HrCreate, db: Session=Depends(getDatabase)):
    # print("go here")
    return HrController.createHr(request=request, db=db)

@router.get("/hr/{hrId}")
def getHrById(hrId: int, db: Session=Depends(getDatabase)):
    return HrController.getHrById(hrId=hrId, db=db)

@router.put("/hr/update/{hrId}")
def updateHr(hrId: int, hr: UpdateHr, db: Session = Depends(getDatabase)):
    return HrController.updateHr(hrId=hrId, hr=hr, db=db)

@router.delete("/hr/delete/{hrId}")
def deleteHr(hrId: int, db: Session = Depends(getDatabase)):
    return HrController.deleteHr(hrId=hrId, db=db)