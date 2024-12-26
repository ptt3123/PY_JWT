from abc import abstractmethod

from ..user_service import UserService
from DAO.UserDAO import UserRegisterDAO


class UserRegisterService(UserService):
    """"""

    def __init__(self, user_register_dao: UserRegisterDAO):
        self._user_register_dao = user_register_dao

    @abstractmethod
    async def register(self, user: dict):
        pass