from fastapi import Depends

from DAO.UserDAO import UserLoginDAO
from exception import METHOD_NOT_FOUND_EXCEPTION
from Service.UserService.UserLoginService import *
from ..DAODependency import get_user_login_dao


async def get_login_service(
        method: str,
        user_login_dao: UserLoginDAO = Depends(get_user_login_dao)) \
        -> UserLoginService:

    """
    Factory Design Pattern For Chose What Service To Return
    (:class:`UserLoginByUsernameService` or :class:`UserLoginByEmailService`),
    Can Raise Exception

    :param method: (:class:`str`)
    :param user_login_dao: (:class:`UserLoginDAO`)
    :return: (:class:`UserLoginService`)
    """

    if method == "username":
        return UserLoginByUsernameService(user_login_dao)

    elif method == "email":
        return UserLoginByEmailService(user_login_dao)

    else:
        raise METHOD_NOT_FOUND_EXCEPTION