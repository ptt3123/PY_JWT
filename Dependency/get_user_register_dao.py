from fastapi import Depends

from DAO.UserDAO import UserRegisterDAO
from Service.AsyncSessionProviderService import AsyncSessionProviderService


async def get_user_register_dao(
        session_provider_service: AsyncSessionProviderService = Depends()) \
        -> UserRegisterDAO:
    """"""

    return UserRegisterDAO(session_provider_service)