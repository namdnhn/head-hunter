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
        cv: CreateCv,
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
            introduce=cv.introduce or '',
            email=cv.email or '',
            phone=cv.phone or '',
            gender=cv.gender or '',
            date_of_birth=cv.date_of_birth or '',
            role=cv.role or '',
            year_experience=cv.year_experience or '',
            degree=cv.degree or '',
            current_address=cv.current_address or '',
            skill=cv.skill or '',
            language=cv.language or '',
            cv=cv.cv or '',
            avatar=cv.avatar or ''
        )
        db.add(db_cv)
        db.commit()
        db.refresh(db_cv)

        # Assuming experience_list and education_list are lists of dictionaries
        for exp in experiences:
            db_exp = Experience(
                cv_id=db_cv.id,
                company=exp.get('company', ''),
                time=exp.get('time', '')
            )
            db.add(db_exp)

        # Create educations
        for edu in educations:
            db_edu = Education(
                cv_id=db_cv.id,
                school=edu.get('school', ''),
                time=edu.get('time', ''),
                department=edu.get('department', '')
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
        return db.query(CvModel).options(joinedload(CvModel.experiences), joinedload(CvModel.educations)).filter(CvModel.user_id == userId).first()

    def updateCv(
        cvId: int,
        experiences: list[dict],
        educations: list[dict],
        cv: UpdateCv,
        db: Session = Depends(getDatabase),
    ):
        dbCv = db.query(CvModel).filter(CvModel.id == cvId).first()
        if cv.user_id is not None:
            dbCv.user_id = cv.user_id
        if cv.introduce is not None:
            dbCv.introduce = cv.introduce
        if cv.email is not None:
            dbCv.email = cv.email
        if cv.phone is not None:
            dbCv.phone = cv.phone
        if cv.gender is not None:
            dbCv.gender = cv.gender
        if cv.date_of_birth is not None:
            dbCv.date_of_birth = cv.date_of_birth
        if cv.role is not None:
            dbCv.role = cv.role
        if cv.year_experience is not None:
            dbCv.year_experience = cv.year_experience
        if cv.degree is not None:
            dbCv.degree = cv.degree
        if cv.current_address is not None:
            dbCv.current_address = cv.current_address
        if cv.skill is not None:
            dbCv.skill = cv.skill
        if cv.language is not None:
            dbCv.language = cv.language
        if cv.cv is not None:
            dbCv.cv = cv.cv
        if cv.avatar is not None:
            dbCv.avatar = cv.avatar


        db.query(Experience).filter(Experience.cv_id == cvId).delete()
        for exp_data in experiences:
            newExp = Experience(
                cv_id = cvId,
                company=exp_data['company'],
                time=exp_data['time']
            )
            db.add(newExp)
            db.commit()
            db.refresh(newExp)
        
            

        # Update educations
        db.query(Education).filter(Education.cv_id == cvId).delete()
        for edu_data in educations:
            newEdu = Education(
                cv_id = cvId,
                school=edu_data['school'],
                time=edu_data['time'],
                department=edu_data['department']
            )
            db.add(newEdu)
            db.commit()
            db.refresh(newEdu)                

        db.commit()
        return {"msg": "Updated"}

    def deleteCv(cvId: int, db: Session = Depends(getDatabase)):
        dbCv = db.query(CvModel).filter(CvModel.id == cvId).first()
        db.delete(dbCv)
        db.commit()
        return {"msg": "Deleted"}
