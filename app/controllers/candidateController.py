from fastapi import Depends, HTTPException
from models.cv import CvModel
from models.company import CompanyModel
from models.user import UserModel
from models.candidate import CandidateModel
# from schemas.candidateSchema import candidateCreate, Updatecandidate
from database import getDatabase
from sqlalchemy.orm import Session


class candidateController:
    @staticmethod
    # def createCandidate(request: candidateCreate, db: Session):
    #     newcandidate = CandidateModel(
    #         user_id = request.user_id,
    #         company_id=request.company_id,
    #     )
    #     db.add(newcandidate)
    #     db.commit()
    #     db.refresh(newcandidate)
    #     return newcandidate
    
    # def getcandidateById(candidateId: int, db: Session = Depends(getDatabase)):
    #     return db.query(candidateModel).filter(candidateModel.id == candidateId).first()

    def getCandidateInfo(candidateId: int, db: Session = Depends(getDatabase)):
        candidate = (
            db.query(UserModel, CvModel)
            .join(CandidateModel, UserModel.id == CandidateModel.user_id)
            .join(CvModel, CvModel.id == CandidateModel.cv_id)
            .filter(UserModel.id == candidateId)
            .first()
        )

        if not candidate:
            raise HTTPException(status_code=404, detail="Candidate not found")

        # Format the candidate information as per the specified structure
        candidate_info = {
            "name": candidate.UserModel.fullname,
            "position": candidate.CvModel.position,
            "location": candidate.location,  # You may need to retrieve this information from the user model
            "date_of_birth": candidate.UserModel.date_of_birth.strftime("%d-%m-%Y"),
            "skills": candidate.CvModel.skill.split(", "),
            "email": candidate.UserModel.email,
            "phone_number": candidate.UserModel.phone,
            "gender": candidate.UserModel.gender,  # You may need to retrieve this information from the user model
            "degree": candidate.CvModel.degree,  # You may need to retrieve this information from the user model
            "experience": candidate.CvModel.experience,  # You need to fetch this information from the database
            "education": candidate.CvModel.education,  # You need to fetch this information from the database
            "language": candidate.CvModel.language,  # You may need to retrieve this information from the user model
            "cv": [candidate.CvModel.image_path],  # Assuming image_path is the URL for the PDF
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
    
