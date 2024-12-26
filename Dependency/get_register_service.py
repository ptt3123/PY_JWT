from fastapi import Depends

from DAO.UserDAO import UserRegisterDAO
from Service.UserService.UserRegisterService import UserRegisterService


async def get_register_service(user_register_dao: UserRegisterDAO = Depends()) \
        -> UserRegisterService:
    """"""

    return UserRegisterService(user_register_dao)
