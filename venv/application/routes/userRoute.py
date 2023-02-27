from fastapi import APIRouter
from application.controllers.userController import UserService

router = APIRouter(prefix="/users", tags=["Users"])


# # !http://localhost:5000/users
@router.get('/')
async def getAllUsers():
    return UserService.get_allUser()


# # !http://localhost:5000/users/me
@router.get('/me')
async def getSingleUser():
    return UserService.getUser()
