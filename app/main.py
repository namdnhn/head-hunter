from fastapi import FastAPI
from models.hr import HrModel
from models.candidate import CandidateModel
from database import Base, engine
from routes import companyRouter, userRouter, hrRouter, cvRouter
from models.application import ApplicationModel
from models.post import PostModel
from fastapi import Depends
from controllers.userController import reusable_oauth2, isTokenInvalidated
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(companyRouter.router, prefix="/api")
app.include_router(userRouter.router, prefix="/api")
app.include_router(hrRouter.router, prefix="/api")
app.include_router(cvRouter.router, prefix="/api")
# app.include_router(messageRouter.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*", "sentry-trace", "baggage"],
)


@app.get("/api/ping")
def ping(data: str = Depends(reusable_oauth2)):
    if isTokenInvalidated(data):
        return "pong"
