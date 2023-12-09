from fastapi import Depends
from database import getDatabase
from models.company import CompanyModel
from schemas.companySchema import CompanyCreate
from schemas.companySchema import CompanyUpdate
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
            logo=request.logo,
        )
        db.add(newCompany)
        db.commit()
        db.refresh(newCompany)
        return newCompany
    
    @staticmethod
    def updateCompany(company_id: int, request: CompanyUpdate, db: Session):
        company = db.query(CompanyModel).filter(CompanyModel.id == company_id).first()
        if not company:
            return None  # or raise an exception

        for var, value in vars(request).items():
            if value is not None:  # we only update fields that are provided in the request
                setattr(company, var, value)

        db.commit()
        db.refresh(company)
        return company

    def getCompanyById(companyId: int, db: Session = Depends(getDatabase)):
        return db.query(CompanyModel).filter(CompanyModel.id == companyId).first()
    
    def getCompanyByUserId(userId: int, db: Session = Depends(getDatabase)):
        return db.query(CompanyModel).filter(CompanyModel.user_id == userId).first()
    
    def getAllCompanies(db: Session):
        return db.query(CompanyModel).all()
