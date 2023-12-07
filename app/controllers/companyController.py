from fastapi import Depends
from database import getDatabase
from models.company import CompanyModel
from schemas.companySchema import CompanyCreate
from sqlalchemy.orm import Session


class CompanyController:
    @staticmethod
    def createCompany(request: CompanyCreate, db: Session):
        newCompany = CompanyModel(
            user_id=request.user_id,
            job_quantity=request.job_quantity,
            name=request.name,
            address=request.address,
            founded_year=request.founded_year,
            employee_quantity=request.employee_quantity,
            description=request.description,
            contact=request.contact,
        )
        db.add(newCompany)
        db.commit()
        db.refresh(newCompany)
        return newCompany

    def getCompanyById(companyId: int, db: Session = Depends(getDatabase)):
        return db.query(CompanyModel).filter(CompanyModel.id == companyId).first()
