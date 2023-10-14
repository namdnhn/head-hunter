from fastapi import Depends, HTTPException
from models.company import CompanyModel
from models.user import UserModel
from models.hr import HrModel
from schemas.hrSchema import HrCreate, UpdateHr
from database import getDatabase
from sqlalchemy.orm import Session


class HrController:
    @staticmethod
    def createHr(request: HrCreate, db: Session):
        newHr = HrModel(
            user_id = request.user_id,
            company_id=request.company_id,
        )
        db.add(newHr)
        db.commit()
        db.refresh(newHr)
        return newHr
    
    def getHrById(hrId: int, db: Session = Depends(getDatabase)):
        return db.query(HrModel).filter(HrModel.id == hrId).first()

    def updateHr(hrId: int, hr: UpdateHr, db: Session):
        dbHrId = db.query(HrModel).filter(HrModel.id == hrId).first()

        if hr.user_id is not None:
            # Check if user_id exists in the database
            user = db.query(UserModel).filter(UserModel.id == hr.user_id).first()
            if user is not None:
                dbHrId.user_id = hr.user_id
            else:
                raise HTTPException(status_code=400, detail="Invalid user_id")

        if hr.company_id is not None:
            # Check if company_id exists in the database
            company = db.query(CompanyModel).filter(CompanyModel.id == hr.company_id).first()
            if company is not None:
                dbHrId.company_id = hr.company_id
            else:
                raise HTTPException(status_code=400, detail="Invalid company_id")
        db.commit()
        return {"msg": "Updated"}
    
    def deleteHr(hrId: int, db: Session):
        dbHrId = db.query(HrModel).filter(HrModel.id == hrId).first()
        db.delete(dbHrId)
        db.commit()
        return {"msg": "Deleted"}
    
