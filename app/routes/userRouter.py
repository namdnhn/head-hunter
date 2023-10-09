from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from database import getDatabase
from controllers.userController import UserController, verifyToken
from schemas.userSchema import RegisterUser, Login, UpdateUser
from models.user import UserModel

router = APIRouter(
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

@router.post("/login")
def login(
        request: Login,
        db: Session = Depends(getDatabase),
    ):
    return UserController.login(request=request, db=db)

@router.post("/register")
def register(user: RegisterUser, db: Session=Depends(getDatabase)):
    return UserController.create_user(user=user, db=db)

@router.post("/logout")
def logout(response: str = Depends(UserController.logout)):
    return response

@router.get("/me")
def getMe(current_user: UserModel = Depends(verifyToken)):
    return current_user

@router.get("/user/all")
def getAllUser(db: Session=Depends(getDatabase)):
    return UserController.getAllUser(db=db)

@router.get("/user/{userId}")
def getUserById(userId: int, db: Session=Depends(getDatabase)):
    return UserController.getUserById(userId=userId, db=db)

@router.put("/user/update/{userId}")
def updateUser(userId: int, user: UpdateUser, db: Session = Depends(getDatabase)):
    return UserController.updateUser(userId=userId, user=user, db=db)

@router.delete("/user/delete/{userId}")
def deleteUser(userId: int, db: Session = Depends(getDatabase)):
    return UserController.deleteUser(userId=userId, db=db)