from fastapi import Depends

from exception import METHOD_NOT_FOUND_EXCEPTION
from DAO.UserDAO import UserLoginDAO
from Service.UserService.UserLoginService import *


def get_login_service(method: str,
                      user_login_dao: UserLoginDAO = Depends()) \
        -> UserLoginService:
    """"""

    if method == "username":
        return UserLoginByUsernameService(user_login_dao)

    elif method == "email":
        return UserLoginByEmailService(user_login_dao)

    else:
        raise METHOD_NOT_FOUND_EXCEPTION