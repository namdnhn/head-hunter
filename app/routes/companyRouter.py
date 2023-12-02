from fastapi import APIRouter, Depends, Response
from schemas.companySchema import CompanyCreate
from sqlalchemy.orm import Session
from database import getDatabase
from controllers.companyController import CompanyController


router = APIRouter(
    prefix="/company",
    tags=["company"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def create_company(request: CompanyCreate, db: Session=Depends(getDatabase)):
    return CompanyController.createCompany(request=request, db=db)

@router.get("/{companyId}")
def get_company_by_id(companyId: int, db: Session=Depends(getDatabase)):
    return CompanyController.getCompanyById(companyId=companyId, db=db)