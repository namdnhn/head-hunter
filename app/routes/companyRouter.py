from fastapi import APIRouter, Depends, Response
from schemas.companySchema import CompanyCreate
from sqlalchemy.orm import Session
from database import getDatabase
from controllers.companyController import CompanyController
from schemas.companySchema import CompanyCreate, CompanyUpdate


router = APIRouter(
    prefix="/company",
    tags=["company"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def create_company(request: CompanyCreate, db: Session=Depends(getDatabase)):
    return CompanyController.createCompany(request=request, db=db)

@router.put("/{company_id}")
async def update_company(company_id: int, request: CompanyUpdate, db: Session = Depends(getDatabase)):
    return CompanyController.updateCompany(company_id=company_id, request=request, db=db)

@router.get("/{companyId}")
def get_company_by_id(companyId: int, db: Session=Depends(getDatabase)):
    return CompanyController.getCompanyById(companyId=companyId, db=db)

@router.get("/user/{userId}")
def get_company_by_userId(userId: int, db: Session=Depends(getDatabase)):
    return CompanyController.getCompanyByUserId(userId=userId, db=db)

@router.get("/")
def get_all_companies(db: Session = Depends(getDatabase)):
    return CompanyController.getAllCompanies(db=db)