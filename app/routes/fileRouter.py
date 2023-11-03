from fastapi import APIRouter, Depends, Response
from schemas.companySchema import CompanyCreate
from sqlalchemy.orm import Session
from database import getDatabase
from controllers.companyController import CompanyController
from schemas.fileSchema import FileCreate
from models.file import FileModel


router = APIRouter(
    prefix="/file",
    tags=["file"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def createFile(request: FileCreate, db: Session=Depends(getDatabase)):
    newFile = FileModel(
        file_name = request.file_name,
        file_path = request.file_path,
        file_size = request.file_size,
        file_type = request.file_type,
        created_by = request.created_by
    )
    db.add(newFile)
    db.commit()
    db.refresh(newFile)
    return newFile