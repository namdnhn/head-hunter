from fastapi import FastAPI
from database import Base, engine
from routes import companyRouter, userRouter
from models.application import ApplicationModel
from models.post import PostModel
from fastapi import Depends
from controllers.userController import reusable_oauth2, isTokenInvalidated

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(companyRouter.router, prefix="/api")
app.include_router(userRouter.router, prefix="/api")

@app.get("/api/ping")
def ping(data: str = Depends(reusable_oauth2)):
    if(isTokenInvalidated(data)):
        return "pong"