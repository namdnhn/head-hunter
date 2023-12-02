from fastapi import APIRouter, Depends, Response
from controllers.cvController import CvController
from schemas.cvSchema import CvCreate
from sqlalchemy.orm import Session
from database import getDatabase


router = APIRouter(
    prefix="/cv",
    tags=["cv"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def createCv(request: CvCreate, db: Session=Depends(getDatabase)):
    # print("go here")
    return CvController.createCv(request=request, db=db)

@router.get("/cv/{cvId}")
def getCvById(cvId: int, db: Session=Depends(getDatabase)):
    return CvController.getCvById(cvId=cvId, db=db)

# @router.put("/hr/update/{hrId}")
# def updateHr(hrId: int, hr: UpdateHr, db: Session = Depends(getDatabase)):
#     return HrController.updateHr(hrId=hrId, hr=hr, db=db)

# @router.delete("/hr/delete/{hrId}")
# def deleteHr(hrId: int, db: Session = Depends(getDatabase)):
#     return HrController.deleteHr(hrId=hrId, db=db)