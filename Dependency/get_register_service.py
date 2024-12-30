from fastapi import Depends

from DAO.UserDAO import UserRegisterDAO
from Service.UserService.UserRegisterService import UserRegisterService
from .get_user_register_dao import get_user_register_dao

async def get_register_service(
        user_register_dao: UserRegisterDAO = Depends(get_user_register_dao)) \
        -> UserRegisterService:
    """"""

    return UserRegisterService(user_register_dao)
