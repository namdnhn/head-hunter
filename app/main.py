from fastapi import FastAPI
from database import Base, engine
from routes import companyRouter
from models.application import ApplicationModel

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(companyRouter.router, prefix="/api")
