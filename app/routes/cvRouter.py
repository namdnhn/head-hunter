from typing import Optional
from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from controllers.cvController import CvController
from database import getDatabase
from schemas.cvSchema import CreateCv, UpdateCv

router = APIRouter(
    prefix="/cv",
    tags=["CV"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{cvId}")
def get_cv_by_cv_id(cvId: int, db: Session = Depends(getDatabase)):
    return CvController.getCvByCvId(cvId=cvId, db=db)


@router.get("/user/{userId}")
def get_cv_by_user_id(userId: int, db: Session = Depends(getDatabase)):
    return CvController.getCvByUserId(userId=userId, db=db)


@router.post("/create")
def create_cv(experiences: list[dict], educations: list[dict], cv: CreateCv = Depends(), db: Session = Depends(getDatabase)):
    return CvController.createCv(experiences=experiences, educations=educations, cv=cv, db=db)

@router.put("/update/{cvId}")
def update_cv(
    cvId: int,
    cv: UpdateCv = Depends(),
    db: Session = Depends(getDatabase),
):
    return CvController.updateCv(cvId=cvId, cv=cv, db=db)


@router.delete("/delete/{cvId}")
def delete_cv(
    cvId: int,
    db: Session = Depends(getDatabase),
):
    return CvController.deleteCv(cvId=cvId, db=db)
