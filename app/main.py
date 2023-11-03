from fastapi import FastAPI
from database import Base, engine
from routes import companyRouter, userRouter, messageRouter, fileRouter
from models.application import ApplicationModel
from models.post import PostModel
from models.message import MessageModel
from models.file import FileModel
from models.conversation import ConversationModel
from models.participant import ParticipantModel
from fastapi import Depends
from controllers.userController import reusable_oauth2, isTokenInvalidated

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(companyRouter.router, prefix="/api")
app.include_router(userRouter.router, prefix="/api")
app.include_router(messageRouter.router, prefix="")
app.include_router(fileRouter.router, prefix="")

@app.get("/api/ping")
def ping(data: str = Depends(reusable_oauth2)):
    if(isTokenInvalidated(data)):
        return "pong"