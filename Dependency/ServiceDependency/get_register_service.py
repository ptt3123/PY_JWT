from fastapi import Depends

from DAO.UserDAO import UserRegisterDAO
from Service.UserService.UserRegisterService import UserRegisterService
from ..DAODependency import get_user_register_dao

async def get_register_service(
        user_register_dao: UserRegisterDAO = Depends(get_user_register_dao)) \
        -> UserRegisterService:

    """
    Get RegisterService

    :param user_register_dao: (:class:`UserRegisterDAO`)
    :return: (:class:`UserRegisterService`)
    """

    return UserRegisterService(user_register_dao)
