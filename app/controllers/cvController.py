import json
from pstats import Stats
import statistics
from typing import Optional
from models.user import UserModel
from schemas.cvSchema import CreateCv, UpdateCv
from models.cv import CvModel, Education, Experience
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, UploadFile
from database import getDatabase
from sqlalchemy.orm import joinedload
from fastapi import Depends, HTTPException, status


class CvController:
    # def createCv(
    #     cv: CreateCv = Depends(),
    #     db: Session = Depends(getDatabase),
    # ):
    #     db_cv = CvModel(
    #         user_id=cv.user_id,
    #         image_path=cv.image_path,
    #         experience=cv.experience,
    #         position=cv.position,
    #         skill=cv.skill,
    #         education=cv.education,
    #         achivement=cv.achivement,
    #         activity=cv.activity,
    #     )
    #     db.add(db_cv)
    #     db.commit()
    #     db.refresh(db_cv)
    #     return db_cv

    def createCv(
        experiences: list[dict],
        educations: list[dict],
        cv: CreateCv = Depends(),
        db: Session = Depends(getDatabase),
    ):
        # Assuming cv.experience and cv.education are strings representing JSON arrays
        # experience_list = json.loads(cv.experience)
        # education_list = json.loads(cv.education)
        user = db.query(UserModel).filter(UserModel.id == cv.user_id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
        )    
        db_cv = CvModel(
            user_id=cv.user_id,
            image_path=cv.image_path,
            pdf_path=cv.pdf_path,
            location=cv.location,
            position=cv.position,
            skill=cv.skill,
            degree=cv.degree,
            achivement=cv.achivement,
            activity=cv.activity,
            language=cv.language
        )
        db.add(db_cv)
        db.commit()
        db.refresh(db_cv)

        # Assuming experience_list and education_list are lists of dictionaries
        for exp in experiences:
            db_exp = Experience(
                cv_id=db_cv.id,
                company=exp['company'],
                time=exp['time']  
            )
            db.add(db_exp)

        # Create educations
        for edu in educations:
            db_edu = Education(
                cv_id=db_cv.id,
                school=edu['school'],
                time=edu['time'],
                department=edu['department']    
            )
            db.add(db_edu)

        db.commit()
        db.refresh(db_cv)

        result_cv = (
            db.query(CvModel)
            .options(
                joinedload(CvModel.experiences),
                joinedload(CvModel.educations),
            )
            .filter(CvModel.id == db_cv.id)
            .first()
        )

        return result_cv

    # def getCvByCvId(cvId: int, db: Session = Depends(getDatabase)):
    #     return db.query(CvModel).filter(CvModel.id == cvId).first()

    def getCvByCvId(cvId: int, db: Session = Depends(getDatabase)):
        return (
            db.query(CvModel)
            .options(joinedload(CvModel.experiences), joinedload(CvModel.educations))
            .filter(CvModel.id == cvId)
            .first()
        )

    def getCvByUserId(userId: int, db: Session = Depends(getDatabase)):
        return db.query(CvModel).filter(CvModel.user_id == userId).all()

    def updateCv(
        cvId: int,
        cv: UpdateCv,
        db: Session = Depends(getDatabase),
    ):
        dbCv = db.query(CvModel).filter(CvModel.id == cvId).first()
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
        if cv.image_path is not None:
            dbCv.image_path = cv.image_path

        db.commit()
        return {"msg": "Updated"}

    def deleteCv(cvId: int, db: Session = Depends(getDatabase)):
        dbCv = db.query(CvModel).filter(CvModel.id == cvId).first()
        db.delete(dbCv)
        db.commit()
        return {"msg": "Deleted"}
