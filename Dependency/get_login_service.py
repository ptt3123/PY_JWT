from fastapi import Depends

from DAO.UserDAO import UserLoginDAO
from exception import METHOD_NOT_FOUND_EXCEPTION
from Service.UserService.UserLoginService import *
from .get_user_login_dao import get_user_login_dao


async def get_login_service(
        method: str,
        user_login_dao: UserLoginDAO = Depends(get_user_login_dao)) \
        -> UserLoginService:
    """"""

    if method == "username":
        return UserLoginByUsernameService(user_login_dao)

    elif method == "email":
        return UserLoginByEmailService(user_login_dao)

    else:
        raise METHOD_NOT_FOUND_EXCEPTION