from fastapi import Depends

from DAO.UserDAO import UserLoginDAO
from Service.AsyncSessionProviderService import AsyncSessionProviderService


async def get_user_login_dao(
        session_provider_service: AsyncSessionProviderService = Depends()) \
        -> UserLoginDAO:
    """
    Get UserLoginDAO

    :param session_provider_service: (:class:`AsyncSessionProviderService`)
    :return: (:class:`UserLoginDAO`)
    """

    return UserLoginDAO(session_provider_service)