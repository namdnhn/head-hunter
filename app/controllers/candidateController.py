from fastapi import Depends, HTTPException
from schemas.candidateSchema import CandidateCreate
from models.cv import CvModel, Education, Experience
from models.user import UserModel
from models.candidate import CandidateModel
from database import getDatabase
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from fastapi import Depends, HTTPException, status


class candidateController:
    @staticmethod
    def createCandidate(request: CandidateCreate, db: Session):
        newcandidate = CandidateModel(
            user_id = request.user_id,
            cv_id=request.cv_id,
        )
        db.add(newcandidate)
        db.commit()
        db.refresh(newcandidate)
        return newcandidate
    
    def getcandidateById(candidateId: int, db: Session = Depends(getDatabase)):
        return db.query(CandidateModel).filter(CandidateModel.id == candidateId).first()
    
    def getCandidateInfo(candidate_id: int, db: Session = Depends(getDatabase)):
    # Query user information
        candidate = db.query(CandidateModel).filter(CandidateModel.id == candidate_id).first()
        user = db.query(UserModel).filter(UserModel.id == candidate.user_id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        cv = (
            db.query(CvModel)
            .filter(CvModel.user_id == user.id)
            .first()
        )
        experiences = db.query(Experience).filter(Experience.cv_id == cv.id)
        educations = db.query(Education).filter(Education.cv_id == cv.id)
        # # Query CV information with related experiences and educations
        # return cv,experiences, educations
        if cv is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="CV not found",
            )

        # Format the result
        candidate_info = {
            "name": user.fullname,
            "position": cv.position,
            "location": cv.location,
            "date_of_birth": user.date_of_birth.strftime("%d-%m-%Y"),
            "skills": cv.skill.split(','),  # Assuming skills are stored as a comma-separated string
            "email": user.email,
            "phone_number": user.phone,
            "gender": user.gender,
            "degree": cv.degree,
            "experience": [
                {"company": exp.company, "time": exp.time}
                for exp in experiences
            ],
            # "experience": experiences,
            "education": [
                {
                    "school": edu.school,
                    "time": edu.time,
                    "department": edu.department,
                }
                for edu in educations
            ],
            # "education": educations,
            "language": cv.language.split(','),  # Assuming languages are stored as a comma-separated string
            "cv": [cv.pdf_path],  # Assuming there's one PDF URL for simplicity
        }

        return candidate_info
    
    # def updatecandidate(candidateId: int, candidate: Updatecandidate, db: Session):
    #     dbcandidateId = db.query(candidateModel).filter(candidateModel.id == candidateId).first()

    #     if candidate.user_id is not None:
    #         # Check if user_id exists in the database
    #         user = db.query(UserModel).filter(UserModel.id == candidate.user_id).first()
    #         if user is not None:
    #             dbcandidateId.user_id = candidate.user_id
    #         else:
    #             raise HTTPException(status_code=400, detail="Invalid user_id")

    #     if candidate.company_id is not None:
    #         # Check if company_id exists in the database
    #         company = db.query(CompanyModel).filter(CompanyModel.id == candidate.company_id).first()
    #         if company is not None:
    #             dbcandidateId.company_id = candidate.company_id
    #         else:
    #             raise HTTPException(status_code=400, detail="Invalid company_id")
    #     db.commit()
    #     return {"msg": "Updated"}
    
    # def deletecandidate(candidateId: int, db: Session):
    #     dbcandidateId = db.query(candidateModel).filter(candidateModel.id == candidateId).first()
    #     db.delete(dbcandidateId)
    #     db.commit()
    #     return {"msg": "Deleted"}
    
