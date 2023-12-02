from fastapi import Depends, HTTPException
from schemas.cvSchema import CvCreate
from models.cv import CvModel
from models.company import CompanyModel
from models.user import UserModel

# from schemas.cvSchema import CvCreate, UpdateCv
from database import getDatabase
from sqlalchemy.orm import Session


class CvController:
    @staticmethod
    def createCv(request: CvCreate, db: Session):
        newCv = CvModel(
            user_id = request.user_id,
            image_path = request.image_path,
            location = request.location,
            experiences = request.experiences,
            position = request.position,
            skill = request.skill,
            educations = request.educations,
            achivement = request.achivement,
            activity = request.activity,
            language = request.activity
        )
        db.add(newCv)
        db.commit()
        db.refresh(newCv)
        return newCv
    
    def getCvById(CvId: int, db: Session = Depends(getDatabase)):
        return db.query(CvModel).filter(CvModel.id == CvId).first()

    # def updateCv(CvId: int, Cv: UpdateCv, db: Session):
    #     dbCvId = db.query(CvModel).filter(CvModel.id == CvId).first()

    #     if Cv.user_id is not None:
    #         # Check if user_id exists in the database
    #         user = db.query(UserModel).filter(UserModel.id == Cv.user_id).first()
    #         if user is not None:
    #             dbCvId.user_id = Cv.user_id
    #         else:
    #             raise HTTPException(status_code=400, detail="Invalid user_id")

    #     if Cv.company_id is not None:
    #         # Check if company_id exists in the database
    #         company = db.query(CompanyModel).filter(CompanyModel.id == Cv.company_id).first()
    #         if company is not None:
    #             dbCvId.company_id = Cv.company_id
    #         else:
    #             raise HTTPException(status_code=400, detail="Invalid company_id")
    #     db.commit()
    #     return {"msg": "Updated"}
    
    def deleteCv(CvId: int, db: Session):
        dbCvId = db.query(CvModel).filter(CvModel.id == CvId).first()
        db.delete(dbCvId)
        db.commit()
        return {"msg": "Deleted"}
    
