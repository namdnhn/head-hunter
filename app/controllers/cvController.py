from typing import Optional
from schemas.cvSchema import CreateCv, UpdateCv
from models.cv import CvModel
from sqlalchemy.orm import Session
from fastapi import Depends, UploadFile
from database import getDatabase


class CvController:
    def createCv(
        imgFile: UploadFile,
        cv: CreateCv = Depends(),
        db: Session = Depends(getDatabase),
    ):
        if imgFile.content_type.startswith("image"):
            file_path = f"public/{imgFile.filename}"
            with open(file_path, "wb") as image_file:
                image_file.write(imgFile.file.read())
        db_cv = CvModel(
            user_id=cv.user_id,
            image_path=file_path,
            experience=cv.experience,
            position=cv.position,
            skill=cv.skill,
            education=cv.education,
            achivement=cv.achivement,
            activity=cv.activity,
        )
        db.add(db_cv)
        db.commit()
        db.refresh(db_cv)
        return db_cv

    def getCvByCvId(cvId: int, db: Session = Depends(getDatabase)):
        return db.query(CvModel).filter(CvModel.id == cvId).first()

    def getCvByUserId(userId: int, db: Session = Depends(getDatabase)):
        return db.query(CvModel).filter(CvModel.user_id == userId).all()

    def updateCv(
        imgFile: Optional[UploadFile],
        cvId: int,
        cv: UpdateCv,
        db: Session = Depends(getDatabase),
    ):
        dbCv = db.query(CvModel).filter(CvModel.id == cvId).first()
        if imgFile.content_type.startswith("image"):
            file_path = f"public/{imgFile.filename}"
            with open(file_path, "wb") as image_file:
                image_file.write(imgFile.file.read())
            dbCv.image_path = file_path
        if cv.user_id is not None:
            dbCv.user_id = cv.user_id
        if cv.experience is not None:
            dbCv.experience = cv.experience
        if cv.position is not None:
            dbCv.position = cv.position
        if cv.skill is not None:
            dbCv.skill = cv.skill
        if cv.education is not None:
            dbCv.education = cv.education
        if cv.achivement is not None:
            dbCv.achivement = cv.achivement
        if cv.activity is not None:
            dbCv.activity = cv.activity
        db.commit()
        return {"msg": "Updated"}

    def deleteCv(cvId: int, db: Session = Depends(getDatabase)):
        dbCv = db.query(CvModel).filter(CvModel.id == cvId).first()
        db.delete(dbCv)
        db.commit()
        return {"msg": "Deleted"}
