from fastapi import APIRouter
from sqlalchemy.orm import Session
from models.company import CompanyModel
from models.job import JobModel
from database import getDatabase
from fastapi import Depends
from datetime import datetime, timedelta
import pandas
import os



router = APIRouter(
    prefix="/data",
    tags=["Data"],
    responses={404: {"description": "Not found"}},
)


@router.get("/set")
def set_data_into_database(db: Session = Depends(getDatabase)):
    print(os.getcwd())
    data = pandas.read_excel(os.getcwd() + "/data/topcv_data3.xlsx") 
    nameCompany = pandas.DataFrame(data, columns=["Company"])
    logoCompany = pandas.DataFrame(data, columns=["Logo"])
    addressCompany = pandas.DataFrame(data, columns=["Address"])
    roleJob = pandas.DataFrame(data, columns=["Role"])
    salaryJob = pandas.DataFrame(data, columns=["Salary"])
    levelJob = pandas.DataFrame(data, columns=["Level"])
    skillJob = pandas.DataFrame(data, columns=["Skills"])
    quantityJob = pandas.DataFrame(data, columns=["Quantity"])
    descriptionJob = pandas.DataFrame(data, columns=["Description"])
    demandJob = pandas.DataFrame(data, columns=["Demand"])
    benefitJob = pandas.DataFrame(data, columns=["Benefit"])
    for i in range(0, len(nameCompany)):
        newCompany = CompanyModel(
            user_id=1,
            name=nameCompany.Company[i],
            address=addressCompany.Address[i],
        )
        db.add(newCompany)
        db.commit()
        db.refresh(newCompany)
    for i in range(0, len(nameCompany)):
        newJob = JobModel(
            address=addressCompany.Address[i],
            benefit=benefitJob.Benefit[i],
            company_id=i+1,
            require=demandJob.Demand[i],
            description=descriptionJob.Description[i],
            job_detail=descriptionJob.Description[i],
            demand=descriptionJob.Description[i],
            level=levelJob.Level[i],
            quantity=quantityJob.Quantity[i],
            role=roleJob.Role[i],
            salary=salaryJob.Salary[i],
            degree_skill=skillJob.Skills[i],
            deadline=datetime.now() + timedelta(days=7),
            posting_date=datetime.now(),
            company_name=nameCompany.Company[i],
            company_logo=logoCompany.Logo[i],
        )
        db.add(newJob)
        db.commit()
        db.refresh(newJob)
    
    return "Success!"

