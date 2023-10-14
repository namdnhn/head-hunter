from fastapi import Depends
from database import getDatabase
from models.company import CompanyModel
from schemas.companySchema import CompanyCreate
from sqlalchemy.orm import Session


class CompanyController:
    @staticmethod
    def createCompany(request: CompanyCreate, db: Session):
        newCompany = CompanyModel(
            name=request.name,
            description=request.description,
        )
        db.add(newCompany)
        db.commit()
        db.refresh(newCompany)
        return newCompany
    
    def getCompanyById(companyId: int, db: Session = Depends(getDatabase)):
        return db.query(CompanyModel).filter(CompanyModel.id == companyId).first()
    